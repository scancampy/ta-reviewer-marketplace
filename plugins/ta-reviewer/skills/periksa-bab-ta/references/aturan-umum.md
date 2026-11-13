# Aturan umum pemeriksaan (berlaku untuk semua bab)

## 1. Prinsip
- Plugin memberi **umpan balik pendukung**. Nilai akhir dan keputusan tetap di tangan dosen. Sebut ini di laporan.
- **Satu bab per pemeriksaan.** Hanya teks bab yang diperiksa yang dibaca Claude. Bab lain tidak dibaca; konteks dari bab lain datang dari ringkasan dosen (lihat `konteks-lintas-bab.md`).
- **Setiap penilaian wajib berbukti**: nomor halaman PDF (bukan nomor cetak) dan kutipan pendek (maks. ~25 kata) atau uraian singkat. Tidak ada klaim tanpa bukti. Jangan mengarang isi yang tidak ada di teks.
- **"Tidak dapat diverifikasi" bukan "gagal".** Bila suatu butir butuh bab lain yang tidak tersedia, tandai "tidak dapat diverifikasi", nilai komponen hanya dari butir yang dapat diperiksa, dan jangan menurunkan level karena data tidak ada.
- Pilih level yang deskriptornya paling cocok. Bila ragu di antara dua level, pilih yang lebih rendah **hanya jika** keraguan berasal dari kelemahan yang terlihat di teks, bukan dari informasi yang tidak tersedia.
- Bedakan di laporan: butir bertanda **(slide)** (acuan kuliah) dan **(pelengkap)** (indikator tambahan, dapat dinegosiasikan dosen).
- Nada: kolegial dan konstruktif; saran konkret ("pindahkan Gambaran Sistem ke Bab 4"), bukan sekadar "kurang baik".

## 2. Hasil skrip adalah perkiraan
Hasil `analisis_teks.py` (rasio kode, kemiripan, sitasi, tahun sumber, abstrak, lampiran) berasal dari teks hasil ekstraksi PDF. Laporkan sebagai **perkiraan yang dapat dikoreksi dosen**. Jangan menyimpulkan "salin-tempel" atau "sumber tidak bereputasi" dari satu angka.

## 3. N/A
- N/A berarti komponen/indikator memang tidak relevan dengan topik. N/A **bukan** nilai 0 dan **bukan** cara menghindari komponen yang sulit dinilai.
- Jika topik jelas membutuhkan suatu hal tetapi tidak disajikan, nilainya **0**, bukan N/A (contoh: game edukasi tanpa teori pendidikan di Bab 2).
- N/A yang lazim per bab (skrip `hitung_skor.py` memberi peringatan di luar daftar ini):
  Bab 2: komponen 3, 4 · Bab 5: komponen 5, 7 · Bab 7: komponen 4-7. Bab 3 dan 4: N/A berlaku pada indikator/bagian di dalam komponen, bukan komponen utuh. Bab 6: pada indikator topik.
- Sebutkan alasan setiap N/A di laporan agar dosen bisa mengoreksi.
- **Bila bagian yang seharusnya ada tidak ada** (mis. Bab 7 tanpa saran, Bab 5 tanpa hambatan): jangan putuskan N/A sendiri. Laporkan "tidak ditemukan", beri nilai sementara sesuai deskriptor, dan minta dosen memilih N/A atau nilai tersebut.

## 4. Jenis topik (satu daftar untuk semua bab)
Sistem Informasi · Multimedia · AI/ML · Game · Sistem Pakar · Lainnya.
- Simpulkan dari isi bab; tanya dosen **satu kali per sesi** bila tidak jelas, lalu pakai terus.
- Topik gabungan (mis. game dengan AI): pakai gabungan bagian lazim kedua jenis.
- "Lainnya": minta dosen menyebut bagian yang diharapkan, lalu pakai sebagai acuan.
- Bab 6 belum punya indikator khusus Multimedia dan Sistem Pakar: nilai dengan indikator umum dan catat bahwa indikator topiknya belum ada.

## 5. Aturan visual (render halaman)
Skrip `extract_bab.py --render auto` merender halaman yang berisi gambar/diagram/grafik (maks. 12 per pemeriksaan). Lihat gambar hanya untuk butir yang memang butuh penglihatan.
- Bila halaman bergambar lebih banyak dari batas, laporkan bahwa pemeriksaan visual **berbasis sampel**.
- **Gambar proses vs gambar hasil** (dipakai Bab 4 komponen 6 dan Bab 5 komponen 1):
  - *Proses/desain*: diagram alur, ERD, UML, rancangan layar (wireframe/mockup), cuplikan konfigurasi, log, kode, arsitektur.
  - *Hasil*: tangkapan layar aplikasi jadi dengan data nyata, foto produk akhir.
  - Bila ragu (mockup atau tangkapan layar?), tandai **"perlu diverifikasi dosen"**; jangan putuskan sendiri.
- Teks yang hanya terbaca dari gambar sulit dipastikan: jangan menyimpulkan "tidak ada penjelasan" bila hanya teks gambar yang tidak terbaca.

## 6. PDF yang tidak dapat dibaca
Bila skrip melaporkan `pdf_scan: true` atau teks sangat sedikit, **berhenti**: minta dosen mengunggah PDF yang teksnya dapat diseleksi. Jangan menilai.

## 7. Satu bab saja
Bila dosen meminta lebih dari satu bab, minta memilih satu dahulu. Setelah laporan selesai, tawarkan bab berikutnya.

## 8. Tabel keputusan standar yang disepakati
| Hal | Standar |
|---|---|
| Waktu publikasi sumber (Bab 2 komp. 6) | ≥90% sumber ≤5 tahun dan sumber lama ≤2 (teori klasik) → 4; 70-89% → 3; 40-69% → 2; <40% → 1; tahun tak dapat ditelusuri → 0 |
| Bab 3, wawancara/FGD | Indikator kuesioner (ukuran sampel, skala data) dianggap N/A; fase setara dinilai; catat bahwa indikator diadaptasi |
| Bab 4, komp. 3 vs 4 | Komp. 3 menilai ada/tidaknya penjelasan; komp. 4 menilai dasar teori/analisisnya |
| Bab 5, kode sepele | Tidak dihitung dalam rasio penjelasan kode (komp. 4); dinilai di komp. 3 |
| Bab 5, komp. 5 | Level 1 bila tidak ada hambatan disebut tetapi bab memuat proses teknis nyata; Level 0 bila bab tidak memuat proses |
| Bab 7 / abstrak, kemiripan | Pembanding opsional, hanya diproses skrip |
| Lampiran Level 1 | User manual tidak ada = Level 1 apa pun kondisi lain; kekurangan format dicatat |
