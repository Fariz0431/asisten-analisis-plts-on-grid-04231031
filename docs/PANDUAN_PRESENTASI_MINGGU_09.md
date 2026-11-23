# Panduan Presentasi Progres — Evaluasi RAG

## Slide 1 — Judul
Asisten Analisis Kinerja dan Gangguan PLTS On-Grid. Jelaskan tujuan prototipe dan status pengerjaan.

## Slide 2 — Sistem yang sudah tersedia
Tampilkan Streamlit, delapan catatan Knowledge Base, TF-IDF dengan Cosine Similarity, kalkulator PR/CUF/selisih energi, dan LLM opsional.

## Slide 3 — Mengapa perlu evaluasi retrieval
Dokumen yang mirip secara kata belum tentu benar-benar menjawab pertanyaan. Karena itu, pengujian tidak cukup hanya menunjukkan aplikasi dapat berjalan.

## Slide 4 — Rancangan evaluasi 20 pertanyaan
Jelaskan komposisi: pertanyaan satu sumber, lintas dokumen, konteks perhitungan, pertanyaan negatif, dan pertanyaan nilai aktual yang tidak tersedia.

## Slide 5 — Metrik evaluasi
Tampilkan target document coverage, top score, jumlah hasil, dan pemeriksaan pertanyaan negatif. Ambil angka dari file JSON hasil eksekusi, bukan dari perkiraan.

## Slide 6 — Temuan dan tindak lanjut
Tunjukkan pertanyaan yang belum mengambil sumber target, false positive, serta kebutuhan review manual jawaban dan verifikasi artikel asli.

## Naskah singkat
"Pada tahap ini, pengembangan difokuskan pada evaluasi retrieval TF-IDF. Sebanyak 20 pertanyaan disiapkan dan dipetakan terhadap delapan dokumen Knowledge Base. Evaluasi dilakukan untuk melihat apakah dokumen target muncul pada hasil pencarian dan apakah pertanyaan yang tidak memiliki informasi dapat menghasilkan kandidat yang tidak relevan. Hasil evaluasi retrieval tidak dianggap sebagai ukuran akurasi jawaban generatif, sehingga pemeriksaan jawaban dan kecukupan sumber tetap dilakukan secara manual."

## Bukti yang dibawa
- Screenshot aplikasi Streamlit.
- File CSV dan JSON hasil menjalankan skrip evaluasi.
- Satu contoh hasil retrieval yang relevan dan satu contoh pertanyaan negatif.
- Hasil pytest terbaru.
