# Rencana Pengembangan Hybrid Retrieval

## Status
Hybrid Retrieval adalah rencana pengembangan, belum menjadi metode retrieval aktif pada repository ini. Metode aktif tetap TF-IDF dengan cosine similarity.

## Kandidat arsitektur
1. BM25 untuk pencarian leksikal.
2. Dense Retrieval untuk pencarian kemiripan makna menggunakan embeddings.
3. Reciprocal Rank Fusion (RRF) untuk menggabungkan ranking kedua retriever.
4. Pemilihan top-k akhir dan evaluasi relevansi chunk.

## Rencana eksperimen
- Gunakan 20 pertanyaan pada tests/test_cases_minggu_09.json.
- Jalankan TF-IDF baseline dan simpan hasil.
- Implementasikan BM25 serta Dense Retrieval sebagai kandidat terpisah.
- Gabungkan ranking dengan RRF.
- Bandingkan target document coverage, hit@k, hasil pertanyaan negatif, dan penilaian relevansi manual.
- Catat waktu indexing, latency, kebutuhan memori, ukuran model embedding, dan dependensi.
- Jangan menyatakan Hybrid Retrieval lebih akurat jika hasil uji tidak mendukung.

## Kandidat evaluasi
Target document hit@k, Precision@k berdasarkan penilaian relevansi, Recall@k, MRR, false positive, dan latency per query.

Dense Retrieval membutuhkan model embedding. Pemilihan model perlu mempertimbangkan bahasa Indonesia, lisensi, ukuran, dan kemampuan berjalan di lingkungan pengguna.
