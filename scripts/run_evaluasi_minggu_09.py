"""Evaluasi baseline retrieval TF-IDF untuk 20 pertanyaan progres mingguan.

Jalankan dari root repository:
    python scripts/run_evaluasi_minggu_09.py

Skrip mengukur ketercakupan dokumen target, bukan akurasi jawaban generatif.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from plts_assistant.config import settings
from plts_assistant.pipeline import AssistantEngine


def main() -> None:
    cases_path = ROOT / "tests" / "test_cases_minggu_09.json"
    output_dir = ROOT / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    cases = json.loads(cases_path.read_text(encoding="utf-8"))
    engine = AssistantEngine(settings, use_llm=False)

    rows = []
    expected_total = expected_found = 0
    negative_total = negative_correct = 0

    for case in cases:
        hits = engine.search(case["question"])
        retrieved_ids = list(dict.fromkeys(hit.chunk.doc_id for hit in hits))
        expected_ids = case.get("expected_doc_ids", [])
        found_expected = [doc_id for doc_id in expected_ids if doc_id in retrieved_ids]
        expect_no_hit = bool(case.get("expect_no_hit", False))

        expected_total += len(expected_ids)
        expected_found += len(found_expected)
        if expect_no_hit:
            negative_total += 1
            negative_correct += int(len(hits) == 0)

        rows.append({
            "id": case["id"],
            "category": case["category"],
            "question": case["question"],
            "expected_doc_ids": ";".join(expected_ids),
            "retrieved_doc_ids": ";".join(retrieved_ids),
            "target_docs_found": ";".join(found_expected),
            "target_hit_any": bool(found_expected),
            "all_target_docs_found": len(found_expected) == len(expected_ids),
            "expect_no_hit": expect_no_hit,
            "no_hit_check_pass": (len(hits) == 0) if expect_no_hit else "",
            "top_score": hits[0].score if hits else 0.0,
            "result_count": len(hits),
            "answer_review": case.get("answer_review", "Belum dinilai"),
        })

    csv_path = output_dir / "retrieval_evaluation_minggu_09.csv"
    json_path = output_dir / "retrieval_evaluation_minggu_09.json"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "evaluation": "TF-IDF retrieval baseline",
        "question_count": len(cases),
        "document_count": len(engine.documents),
        "chunk_count": len(engine.chunks),
        "top_k": settings.top_k,
        "threshold": settings.retrieval_threshold,
        "expected_target_doc_count": expected_total,
        "found_target_doc_count": expected_found,
        "target_document_coverage": expected_found / expected_total if expected_total else None,
        "negative_no_hit_cases": negative_total,
        "negative_no_hit_correct": negative_correct,
        "interpretation": (
            "Metrik hanya mengukur kemunculan dokumen target. Review manual diperlukan "
            "untuk menilai relevansi jawaban, kutipan, dan abstain pada pertanyaan nilai soiling aktual."
        ),
        "csv_file": str(csv_path.relative_to(ROOT)),
    }
    json_path.write_text(
        json.dumps({"summary": summary, "records": rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"Hasil CSV: {csv_path}")
    print(f"Hasil JSON: {json_path}")


if __name__ == "__main__":
    main()
