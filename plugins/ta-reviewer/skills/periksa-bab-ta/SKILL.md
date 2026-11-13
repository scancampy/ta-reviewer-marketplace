---
name: periksa-bab-ta
description: >-
  Membantu dosen Teknik Informatika memeriksa SATU bab tugas akhir mahasiswa (Bab 1 Pendahuluan, 2 Landasan Teori,
  3 Analisis, 4 Perancangan, 5 Implementasi, 6 Evaluasi, 7 Kesimpulan dan Saran) atau bagian pendukung (Abstrak,
  Daftar Pustaka, Lampiran) terhadap rubrik penilaian per bab, lengkap dengan bukti halaman, skor, dan saran perbaikan.
  Gunakan skill ini setiap kali dosen mengunggah PDF tugas akhir/skripsi/laporan TA (satu bab atau 7 bab sekaligus), atau
  menyebut memeriksa, menilai, mereview, merevisi, atau memberi feedback pada bab, rubrik, tinjauan pustaka, uji coba,
  kesimpulan, daftar pustaka, abstrak atau lampiran, bahkan bila tidak menyebut kata "rubrik".
---

# Periksa Bab Tugas Akhir

Memberi **umpan balik pendukung** untuk dosen. Nilai akhir dan keputusan tetap di tangan dosen.
Memeriksa **satu bab per permintaan**, dan hanya rubrik bab itu yang dimuat, agar komputasi ringan.

## Peta file (muat hanya yang dibutuhkan)

| File | Kapan dibaca |
|---|---|
| `references/aturan-umum.md` | Selalu, sekali di awal sesi |
| `references/rubrik-bab{N}-*.md` | Hanya rubrik bab yang diperiksa |
| `references/panduan-per-bab.md` | Hanya bagian bab yang diperiksa (cari judul `## Bab N`) |
| `references/konteks-lintas-bab.md` | Saat meminta ringkasan konteks ke dosen |
| `references/format-laporan.md` | Saat menyusun laporan |
| `references/rubrik-pendukung.md` | Hanya untuk mode pendukung |

Rubrik: 1 `rubrik-bab1-pendahuluan.md` · 2 `rubrik-bab2-landasan-teori.md` · 3 `rubrik-bab3-analisis.md` · 4 `rubrik-bab4-perancangan.md` · 5 `rubrik-bab5-implementasi.md` · 6 `rubrik-bab6-evaluasi.md` · 7 `rubrik-bab7-kesimpulan-dan-saran.md`.

Sinonim nama bab yang diterima: landasan teori = tinjauan pustaka; perancangan = desain; evaluasi = uji coba / pengujian; kesimpulan dan saran = kesimpulan / saran.

## Skrip (folder `scripts/`, jalankan dengan python3)

| Skrip | Fungsi |
|---|---|
| `extract_bab.py` | Pindai struktur bab; ekstrak teks satu bab/bagian; render halaman bergambar; dump teks penuh ke file (untuk skrip saja) |
| `hitung_skor.py` | Hitung nilai akhir dari level tiap komponen, mendukung N/A. **Selalu pakai ini**, jangan menghitung sendiri |
| `analisis_teks.py` | `tahun-sumber`, `sitasi`, `rasio-kode`, `kemiripan`, `abstrak`, `lampiran` (hasilnya perkiraan) |

Dependensi: `pypdf`, `pdfplumber`, `pdf2image` (+ poppler). Lihat `requirements.txt` di akar plugin.

## Alur kerja

1. **Tentukan bab.**
   - Ambil dari permintaan dosen. Bila tidak ada, jalankan `extract_bab.py <pdf> --pindai`.
   - PDF satu bab: pakai bab yang terdeteksi. PDF berisi beberapa bab dan dosen belum menyebut bab: **tanya bab mana, satu saja**.
   - Dosen meminta lebih dari satu bab: minta memilih satu dahulu, lalu tawarkan bab berikutnya setelah selesai.
   - Bila deteksi meragukan atau tidak cocok dengan permintaan, konfirmasi ke dosen sebelum menilai.
2. **Ekstrak** hanya bab itu: `extract_bab.py <pdf> --bab N --out /tmp/periksa [--render auto]`. Perhatikan `peringatan` pada keluaran. Bila PDF hasil scan atau teks kosong: **berhenti** dan minta PDF yang dapat diseleksi.
3. **Muat panduan:** `aturan-umum.md` (bila belum), rubrik bab N, dan bagian bab N di `panduan-per-bab.md`.
4. **Jenis topik** (bab 4, 5, 6): simpulkan dari isi, tanya **sekali per sesi** bila tidak jelas.
5. **Minta konteks lintas bab** dalam satu pesan memakai templat di `konteks-lintas-bab.md`. Bila dosen melewatinya, lanjutkan dan tandai butir terkait "tidak dapat diverifikasi" (bukan gagal).
6. **Jalankan skrip** yang tertera di panduan bab. Hasil skrip adalah perkiraan, laporkan demikian.
7. **Nilai tiap komponen**: pilih level 0-4 (atau N/A dengan alasan) sesuai deskriptor, dengan bukti halaman PDF dan kutipan singkat. Tandai butir (slide) vs (pelengkap). Periksa daftar common mistakes dan konsistensi silang di rubrik.
8. **Hitung skor**: `hitung_skor.py --bab N --level '{"1":3,"2":"N/A",...}'`. Bila ada peringatan N/A tidak lazim, pastikan alasannya tertulis di laporan.
9. **Susun laporan** sesuai `format-laporan.md` di chat. Tutup dengan daftar "perlu diverifikasi dosen" dan tawaran memeriksa bab lain atau membuat dokumen laporan.

## Larangan
- Jangan membaca atau menilai bab selain yang diperiksa. Bab pembanding dan teks penuh hanya diproses skrip.
- Jangan mengarang isi, sitasi, atau halaman. Tanpa bukti → tidak ada klaim.
- Jangan memutuskan N/A atau Level 0 untuk bagian yang tidak ditemukan; serahkan kepada dosen (lihat aturan umum bagian 3).
- Jangan menyatakan sumber "tidak bereputasi", "salin-tempel", atau "overclaim" secara pasti; tandai untuk dosen.
- Jangan menghitung nilai akhir sendiri.
