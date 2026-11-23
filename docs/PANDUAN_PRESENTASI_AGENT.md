# Panduan Presentasi — Tool-Calling Agent dan Retrieval

## Slide 1 — Tujuan pengembangan
Sistem ditingkatkan agar Agent dapat memilih pencarian dokumen atau kalkulator berdasarkan pertanyaan pengguna.

## Slide 2 — Arsitektur Agent
Tampilkan Streamlit → ToolCallingAgent → Search Tool / Calculator Tools → hasil tool → jawaban dengan sumber.

## Slide 3 — Pemanggilan kalkulator
Demonstrasikan pertanyaan CUF: energi 720 kWh, kapasitas 10 kW, durasi 720 jam. Agent harus memanggil calculate_cuf dan mengembalikan 10%.

## Slide 4 — Retrieval
Jelaskan metode aktif TF-IDF + cosine similarity. Top-k 4 dan threshold 0,12 adalah nilai awal, bukan parameter optimum.

## Slide 5 — Retrieval berikutnya
Jelaskan roadmap Hybrid Retrieval: BM25 + Dense Retrieval + Reciprocal Rank Fusion. Tegaskan bahwa metode ini masih rencana, belum diimplementasikan.

## Slide 6 — Evaluasi dan batasan
Tunjukkan output tool_calls, dokumen yang ditemukan, hasil kalkulator, dan mode retrieval-only ketika LLM tidak dikonfigurasi.

## Naskah
"Pada pengembangan ini ditambahkan Tool-Calling Agent. Agent menerima pertanyaan pengguna, lalu model memilih tool yang sesuai. Untuk pertanyaan teori, Agent menggunakan search_knowledge_base dengan retrieval TF-IDF. Untuk pertanyaan hitung, Agent memanggil fungsi kalkulator Python. Jika pertanyaan menggabungkan keduanya, Agent dapat menggunakan kedua tool. Metode retrieval aktif tetap TF-IDF sebagai baseline, sedangkan Hybrid Retrieval direncanakan sebagai eksperimen berikutnya dan akan dibandingkan menggunakan pertanyaan uji yang sama."

## Demo
- Teori: "Apa definisi PR menurut PVsyst?"
- Hitung: "Hitung CUF 720 kWh, 10 kW, 720 jam."
- Gabungan: "Jelaskan PR dan hitung nilai dari data yang saya berikan."
- Tidak cukup data: "Hitung CUF PLTS saya."
- Tidak tersedia: "Apa arti alarm A999?" tanpa manual spesifik.
