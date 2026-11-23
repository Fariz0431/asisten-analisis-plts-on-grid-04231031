# Arsitektur Tool-Calling Agent

## 1. Tujuan
Agent mengatur pemilihan tool berdasarkan pertanyaan pengguna. Agent dapat meminta pencarian Knowledge Base atau memanggil kalkulator Python.

## 2. Komponen
| Komponen | Tugas |
|---|---|
| Streamlit | Menerima pertanyaan dan menampilkan hasil |
| ToolCallingAgent | Menjalankan siklus function calling dan mengatur tool |
| search_knowledge_base | Mengambil chunk melalui baseline TF-IDF |
| calculate_performance_ratio | Menghitung PR secara deterministik |
| calculate_cuf | Menghitung CUF secara deterministik |
| calculate_energy_difference | Menghitung selisih energi |
| LLM opsional | Memilih tool dan menyusun jawaban berdasarkan hasil tool |
| Pydantic | Memvalidasi struktur jawaban dan referensi |

## 3. Alur
1. Pengguna memasukkan pertanyaan di tab Asisten.
2. Jika LLM dan tool calling tersedia, pertanyaan dikirim ke model beserta definisi tool.
3. Model memilih satu atau beberapa tool.
4. Agent menjalankan fungsi Python atau retrieval TF-IDF.
5. Hasil tool dikembalikan ke model dalam pesan tool.
6. Model menyusun JSON akhir.
7. ID sumber dibatasi pada chunk yang benar-benar ditemukan retrieval.
8. Keluaran divalidasi oleh AssistantAnswer dan ditampilkan oleh Streamlit.

## 4. Tool yang tersedia
- search_knowledge_base(query)
- calculate_performance_ratio(energy_grid_kwh, glob_inc_kwh_m2, installed_power_kwp)
- calculate_cuf(energy_kwh, installed_power_kw, period_hours)
- calculate_energy_difference(actual_energy_kwh, reference_energy_kwh)

Kalkulator tidak memperkirakan data yang hilang. Jika parameter wajib tidak tersedia, Agent harus meminta data tambahan.

## 5. Retrieval saat ini
Retrieval aktif tetap TF-IDF dan cosine similarity, dengan konfigurasi awal top-k 4, threshold 0,12, chunk size 1.100 karakter, dan overlap 160 karakter. Konfigurasi ini adalah baseline dan belum dinyatakan optimal.

## 6. Mode tanpa LLM
Jika LLM tidak dikonfigurasi, aplikasi berjalan dalam mode retrieval-only. Pemanggilan tool otomatis oleh Agent tidak aktif. Tab Kalkulator PLTS tetap dapat digunakan secara manual.

## 7. Keterbatasan
- Function calling memerlukan provider dan model yang mendukung tool calling.
- Kompatibilitas endpoint perlu diuji pada provider yang dipilih.
- Retrieval TF-IDF berbasis kecocokan leksikal.
- Hasil retrieval bukan bukti kebenaran.
- Agent tidak mengakses inverter, logger, SCADA, atau sistem kendali.
- Keluaran bukan diagnosis kerusakan definitif.

## 8. Pengujian
Skenario pengujian ada pada tests/test_agent_scenarios.json dan unit test tool berada pada tests/test_agent.py. Pengujian end-to-end dengan provider LLM memerlukan API key lokal yang tidak boleh diunggah.
