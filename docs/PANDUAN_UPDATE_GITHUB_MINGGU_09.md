# Panduan Pembaruan GitHub — Paket Evaluasi

## 1. Jalankan pengujian
Dari terminal VS Code pada root repository:

~~~powershell
python -m pytest -q
python scripts/run_evaluasi_minggu_09.py
~~~

## 2. Periksa keluaran
Buka outputs/retrieval_evaluation_minggu_09.csv dan outputs/retrieval_evaluation_minggu_09.json. Periksa target dokumen, false positive, dan kolom review jawaban.

## 3. Periksa keamanan sebelum commit
Pastikan file .env, API key, token, kredensial, dan data produksi yang bersifat privat tidak ikut diunggah. Jangan menulis nilai soiling aktual tanpa data pengukuran yang dapat ditelusuri.

## 4. Commit hasil
Jika file hasil layak dipublikasikan dan tidak mengandung data sensitif:

~~~powershell
git status
git add tests/test_cases_minggu_09.json scripts/run_evaluasi_minggu_09.py docs/PROGRES_MINGGU_09.md docs/PANDUAN_PRESENTASI_MINGGU_09.md docs/PANDUAN_UPDATE_GITHUB_MINGGU_09.md
git add outputs/retrieval_evaluation_minggu_09.csv outputs/retrieval_evaluation_minggu_09.json
git status
git commit -m "Add week evaluation protocol and retrieval results"
git push
~~~

Jangan menjalankan git add . tanpa memeriksa git status terlebih dahulu.
