from types import SimpleNamespace

import pytest

from plts_assistant.agent import AGENT_TOOLS, ToolCallingAgent
from plts_assistant.documents import Chunk
from plts_assistant.retrieval import SearchResult


class DummyEngine:
    def __init__(self, return_hits=True):
        self.llm_client = None
        self.settings = SimpleNamespace(top_k=4, retrieval_threshold=0.12)
        self.return_hits = return_hits
        self.chunk = Chunk(
            chunk_id="D7-C001",
            doc_id="D7",
            title="Performance Ratio menurut PVsyst",
            source_url="https://www.pvsyst.com/help/project-design/results/performance-ratio-pr.html",
            path="knowledge_base/07_pvsyst_performance_ratio.md",
            text="PR = E_Grid / (GlobInc x PnomPV).",
        )

    def search(self, query, top_k=4, threshold=0.12):
        if not self.return_hits:
            return []
        return [SearchResult(chunk=self.chunk, score=0.8)][:top_k]


def test_agent_exposes_retrieval_and_three_calculator_tools():
    names = {item["function"]["name"] for item in AGENT_TOOLS}
    assert names == {
        "search_knowledge_base",
        "calculate_performance_ratio",
        "calculate_cuf",
        "calculate_energy_difference",
    }


def test_agent_cuf_tool_returns_deterministic_result():
    agent = ToolCallingAgent(DummyEngine())
    payload, hits, calculation = agent._execute_tool(
        "calculate_cuf",
        {"energy_kwh": 720, "installed_power_kw": 10, "period_hours": 720},
        top_k=4,
        threshold=0.12,
    )
    assert payload["persen"] == pytest.approx(10.0)
    assert calculation["persen"] == pytest.approx(10.0)
    assert hits == []


def test_agent_pr_tool_returns_deterministic_result():
    agent = ToolCallingAgent(DummyEngine())
    payload, _, _ = agent._execute_tool(
        "calculate_performance_ratio",
        {"energy_grid_kwh": 900, "glob_inc_kwh_m2": 150, "installed_power_kwp": 10},
        top_k=4,
        threshold=0.12,
    )
    assert payload["persen"] == pytest.approx(60.0)


def test_agent_retrieval_tool_returns_document_chunks():
    agent = ToolCallingAgent(DummyEngine())
    payload, hits, calculation = agent._execute_tool(
        "search_knowledge_base",
        {"query": "performance ratio PVsyst"},
        top_k=4,
        threshold=0.12,
    )
    assert payload["jumlah_hasil"] == 1
    assert payload["hasil"][0]["id_chunk"] == "D7-C001"
    assert len(hits) == 1
    assert calculation is None


def test_agent_unknown_tool_is_rejected():
    agent = ToolCallingAgent(DummyEngine())
    with pytest.raises(ValueError):
        agent._execute_tool("unknown_tool", {}, top_k=4, threshold=0.12)


def test_agent_without_llm_is_explicitly_retrieval_only():
    answer = ToolCallingAgent(DummyEngine()).ask("Apa itu Performance Ratio?")
    assert answer.agent_mode == "retrieval_only"
    assert answer.status == "perlu_verifikasi"
    assert answer.tool_calls == []
    assert answer.sumber[0].id_chunk == "D7-C001"


def test_agent_without_llm_reports_missing_retrieval():
    answer = ToolCallingAgent(DummyEngine(return_hits=False)).ask("Apa arti kode alarm A999?")
    assert answer.agent_mode == "retrieval_only"
    assert answer.status == "informasi_tidak_ditemukan"
    assert answer.sumber == []
