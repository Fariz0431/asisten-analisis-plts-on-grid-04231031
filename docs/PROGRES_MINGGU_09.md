# Progres Minggu Evaluasi — PLTS On-Grid

## Tujuan
Paket ini menambahkan evaluasi retrieval yang lebih terstruktur sebelum pengembangan Agent. Evaluasi memakai 20 pertanyaan yang dipetakan terhadap delapan dokumen Knowledge Base (D1–D8).

## Isi pembaruan
- tests/test_cases_minggu_09.json: 20 pertanyaan satu sumber, lintas dokumen, konteks perhitungan, negatif, dan konteks tanpa nilai aktual.
- scripts/run_evaluasi_minggu_09.py: menjalankan baseline TF-IDF dan menghasilkan CSV serta JSON.
- docs/PANDUAN_PRESENTASI_MINGGU_09.md: susunan slide dan naskah progres.
- docs/PANDUAN_UPDATE_GITHUB_MINGGU_09.md: cara menjalankan evaluasi dan mengunggah hasil.

## Cara menjalankan
Dari root repository:

~~~bash
python scripts/run_evaluasi_minggu_09.py
~~~

Hasil disimpan pada outputs/retrieval_evaluation_minggu_09.csv dan outputs/retrieval_evaluation_minggu_09.json.

## Cara membaca hasil
- Target document coverage menunjukkan berapa banyak dokumen target yang muncul pada hasil top-k.
- Pertanyaan negatif harus ditinjau untuk mendeteksi false positive.
- Pertanyaan nilai soiling aktual dapat mengambil sumber umum untuk konteks, tetapi sumber tersebut tidak membuktikan angka aktual suatu lokasi.
- Kolom answer_review perlu diisi setelah jawaban aplikasi diperiksa secara manual.

## Batas interpretasi
Skrip ini mengukur retrieval, bukan akurasi jawaban LLM, kualitas diagnosis, atau kebenaran data lapangan. Jangan menulis persentase kelulusan sebelum skrip dijalankan pada repository dan lingkungan yang digunakan untuk presentasi.
