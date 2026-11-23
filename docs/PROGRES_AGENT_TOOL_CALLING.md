# Progres Pengembangan — Tool-Calling Agent

## Perubahan implementasi
- Ditambahkan ToolCallingAgent untuk menjalankan function calling melalui LLM opsional.
- Retrieval Knowledge Base disediakan sebagai tool search_knowledge_base.
- Kalkulator PR, CUF, dan selisih energi disediakan sebagai tool terpisah.
- Hasil kalkulator tetap dihitung oleh fungsi Python deterministik.
- Referensi jawaban dibatasi pada chunk yang benar-benar ditemukan retrieval.
- Jawaban memiliki metadata agent_mode dan tool_calls.
- Streamlit menggunakan Agent pada tab Asisten dan tetap menyediakan tab kalkulator manual.
- Jika LLM tidak aktif atau pemanggilan tool gagal, aplikasi turun ke mode retrieval-only dan menyatakan keterbatasan.

## Retrieval
Metode yang benar-benar diimplementasikan tetap TF-IDF + cosine similarity. Hybrid Retrieval baru didokumentasikan sebagai rencana eksperimen dan belum aktif.

## Pemeriksaan setelah perubahan
1. Jalankan pytest.
2. Jalankan Streamlit tanpa LLM dan pastikan mode retrieval-only terlihat.
3. Konfigurasikan provider yang mendukung function calling secara lokal.
4. Uji pertanyaan retrieval, kalkulasi CUF, kalkulasi PR, pertanyaan gabungan, input tidak lengkap, dan kode alarm yang tidak tersedia.
5. Periksa tool_calls pada keluaran terstruktur.

## Batasan
Pengujian unit tool tidak sama dengan pengujian end-to-end dengan LLM/provider. Pemilihan tool harus diuji pada model dan endpoint yang benar-benar digunakan.
