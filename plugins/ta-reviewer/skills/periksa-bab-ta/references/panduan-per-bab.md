# Panduan khusus per bab

Baca **hanya bagian bab yang sedang diperiksa**. Semua path skrip relatif terhadap folder skill (`scripts/`). Folder kerja contoh: `/tmp/periksa`.
Setiap bab: (1) ekstrak, (2) minta konteks lintas bab, (3) jalankan skrip yang tercantum, (4) nilai per komponen, (5) hitung skor dengan `hitung_skor.py`, (6) susun laporan.

---
## Bab 1 Pendahuluan
- Ekstrak: `extract_bab.py <pdf> --bab 1 --out /tmp/periksa` (render tidak perlu).
- Konteks: opsional daftar judul bab dokumen. Tanpa itu, sistematika (komp. 7) dinilai dari kelengkapan (ketujuh bab tercantum dan berdeskripsi); kesesuaian dengan isi dokumen "tidak dapat diverifikasi".
- Aturan khusus:
  - Gambaran Sistem/Proposed Solution **tidak wajib** di Bab 1; uraian solusi yang rinci adalah red flag, bukan kelebihan.
  - Rubrik menyebut "7 komponen"; anggap 7 komponen isi + 1 komponen koherensi/bahasa/format.
  - Red flag "persis sama dengan proposal" tidak bisa dicek: tandai hanya gejalanya (uraian solusi rinci) dan minta dosen memeriksa.
  - Konsistensi silang yang bisa diperiksa di dalam bab: rumusan ← latar belakang, tujuan ↔ rumusan, manfaat ↔ tujuan, ruang lingkup vs tujuan, metodologi vs tujuan. Buat tabel pemetaan rumusan → tujuan.

## Bab 2 Landasan Teori
- Ekstrak bab; lalu ambil daftar pustaka **hanya untuk skrip**:
  1. `extract_bab.py <pdf> --bagian daftar-pustaka --out /tmp/periksa` (bila Bab 2 diunggah terpisah, minta dosen mengunggah halaman daftar pustaka atau PDF-nya).
  2. `analisis_teks.py tahun-sumber --pustaka daftar-pustaka.txt --naskah bab2.txt` → persentase sumber ≤5 tahun, saran level komp. 6 (ambang di `aturan-umum.md`; level 4 butuh pemeriksaan manual bahwa sumber lama adalah teori klasik).
  3. `analisis_teks.py sitasi --naskah bab2.txt --pustaka daftar-pustaka.txt --simpan-dikutip dikutip.txt` → baca **hanya** `dikutip.txt` (entri yang dikutip Bab 2) untuk komp. 7.
- Render: `--render auto` untuk menilai gambar/tabel (komp. 8): penjelasan harus **sebelum** gambar dan panjangnya setara.
- Aturan khusus:
  - N/A komp. 3 dan 4 hanya bila topik memang tidak butuh (lihat aturan umum bagian 3). Tulis alasannya.
  - Komp. 7: nilai reputasi/kompetensi hanya dari yang tertulis (nama jurnal/penerbit, bidang penulis). Sumber meragukan → "perlu diverifikasi dosen", jangan dinyatakan tidak bereputasi.
  - Literature Review: periksa apakah tiap artikel dijadikan subbab sendiri (kesalahan umum), dan apakah posisi penelitian dinyatakan.
  - Konsistensi dengan Bab 1 dan "teori tidak dipakai di bab berikutnya": butuh konteks; bila tidak ada → tidak dapat diverifikasi.

## Bab 3 Analisis
- Ekstrak + `--render auto` (grafik/tabel survei untuk komp. 2).
- Konteks: rumusan masalah (Bab 1). Tanya metode pengumpulan data bila tidak jelas dari teks: kuesioner / wawancara / FGD / lainnya.
- Aturan khusus:
  - Kuesioner: periksa ukuran sampel (minimal 50; 30 batas mutlak) dan jenis skala data. Angka ini **tidak** berlaku untuk wawancara/FGD; di sana indikator kuesioner N/A dan fase setara (pedoman wawancara, pemilihan narasumber) dinilai dengan catatan "diadaptasi".
  - Komp. 2 (penyajian data) memakai gambar: cek baseline hilang, sumbu Y dimanipulasi, cherry picking, jenis grafik tidak tepat. Jika gambar tidak terbaca jelas, tulis "perlu diverifikasi dosen".
  - Buat **tabel penelusuran**: masalah → bukti di analisis kondisi saat ini → pembanding di benchmarking → kebutuhan. Masalah/kebutuhan tanpa mata rantai = temuan.
  - Benchmarking: periksa bahwa tidak hanya membahas sisi buruk dan tidak subjektif.
  - N/A hanya di tingkat indikator di dalam komp. 1.

## Bab 4 Perancangan
- Ekstrak + `--render auto`. Tentukan **jenis topik** (lihat aturan umum bagian 4) sebelum menilai komp. 2.
- Konteks: **daftar kebutuhan sistem (Bab 3)** wajib untuk komp. 1; tanpa itu, nilai komp. 1 hanya dari butir dalam bab (rujukan ke analisis, tabel keterlacakan) dan tulis "pemenuhan seluruh kebutuhan tidak dapat diverifikasi".
- Bagian desain lazim per topik (acuan, bukan daftar baku; lihat tabel di rubrik komp. 2):
  Sistem Informasi: data, proses, antarmuka. Multimedia: data, aset, proses, antarmuka, storyboard. AI: dataset, pra-pemrosesan, ekstraksi fitur, model, pelatihan, evaluasi model, proses dalam aplikasi. Game: data, gameplay, aset, proses, antarmuka. Sistem Pakar: data, aturan, proses, antarmuka.
- Aturan khusus:
  - N/A hanya untuk **bagian desain** di dalam komp. 2 (mis. Process Design tidak wajib), bukan komponen lain.
  - Pembagian komp. 3 vs 4: lihat `aturan-umum.md` bagian 8.
  - Komp. 6: ada tangkapan layar aplikasi jadi / kode final di bab desain? Pakai aturan gambar proses vs hasil.
  - Konsistensi internal: atribut data yang dipakai proses, layar yang menampilkan data. Laporkan ketidakcocokan sebagai temuan konkret.
  - Notasi tidak harus ERD/BPMN; notasi tak umum butuh pengantar singkat. Desain serupa boleh diwakili satu.

## Bab 5 Implementasi
- Ekstrak + `--render auto`.
- Konteks: **daftar bagian desain (Bab 4)** untuk komp. 2 → buat tabel bagian desain → bagian implementasi; tanpa itu nilai dari butir dalam bab.
- Skrip: `analisis_teks.py rasio-kode --teks bab5.txt` → rasio baris penjelasan/kode per listing, listing yang penjelasannya lebih pendek dari kodenya, dugaan hanya komentar, kode mirip. Tinjau halaman yang dirender sebelum menyimpulkan.
- Aturan khusus:
  - Prinsip: **proses lebih penting daripada hasil**. Komp. 1 memakai aturan gambar proses vs hasil dan proporsi halaman bergambar hasil.
  - Komp. 4: kode sepele (login sederhana, CRUD biasa) **dikeluarkan dari rasio**; kode berulang/salin-tempel dicatat.
  - Komp. 3 menilai *apa yang dipilih untuk dijelaskan*; komp. 4 menilai *kualitas penjelasan kode yang ditampilkan*.
  - Komp. 5: laporkan hanya apa yang ada/tidak ada di teks. Jangan menyimpulkan bahwa kegagalan "pasti terjadi". Pakai patokan Level 1/0 di aturan umum; N/A atau Level 0 diputuskan dosen.
  - Komp. 6: gaya tutorial ("klik menu..., lalu pilih...") vs narasi teknis.
  - Komp. 7: N/A pada indikator topik yang tidak berlaku (Multimedia: shooting/dubbing; AI: pipeline; Game: gameplay/aset).

## Bab 6 Evaluasi
- Ekstrak + `--render auto` (tabel/grafik hasil).
- Konteks: rumusan masalah & tujuan (Bab 1), kebutuhan sistem (Bab 3), fitur yang diimplementasikan (Bab 5). Buat tabel pemetaan **tujuan/kebutuhan → bukti di bab ini**; yang tanpa bukti jadi temuan. Tanpa konteks: pencapaian tujuan "tidak dapat diverifikasi".
- Aturan khusus:
  - Periksa **judul subbab**: harus "Verifikasi" dan "Validasi" (kesalahan umum: "6.1 Uji Coba", "6.2 Evaluasi"). Yang diperiksa judul subbab, bukan judul bab (sinonim bab: uji coba).
  - Bila **Validasi tidak ada**, komp. 4-7 (bobot 60) hampir seluruhnya jatuh. Tulis ini di bagian atas laporan agar dosen tahu satu masalah menurunkan banyak komponen.
  - Komp. 5: klaim penelitian diambil dari tujuan (Bab 1) bila ada; bila tidak, ambil dari bab ini dan sebut sebagai asumsi. Pola: klaim pembelajaran → perlu kuis/tes; klaim UX membantu pekerjaan → perlu pengamatan perilaku atau waktu penyelesaian.
  - Komp. 4: ringkas jumlah, karakteristik, dan pelaku partisipan. Tidak ada ambang jumlah partisipan; nilai kecocokan dengan klaim dan metode, tandai "perlu pertimbangan dosen". Jangan pakai ambang 30/50 dari Bab 3.
  - Komp. 3: dua pola: gaya manual pengguna (kalimat perintah langkah demi langkah) dan kegagalan tampil atau tidak (laporkan hanya yang ada di teks). Cari bentuk tabel uji: skenario, masukan, hasil diharapkan, hasil aktual.
  - Komp. 2: jangan turunkan nilai karena tidak semua fitur diuji; yang dinilai adalah keterwakilan. Bila daftar fitur ada, bedakan fitur berulang dari yang berbeda karakter.
  - Komp. 6: pemeriksaan grafik menyesatkan seperti Bab 3.
  - Multimedia dan Sistem Pakar: indikator topik belum ada di rubrik; catat di laporan.

## Bab 7 Kesimpulan dan Saran
- Ekstrak (render tidak perlu).
- Konteks: rumusan masalah & tujuan (Bab 1), ringkasan hasil verifikasi/validasi (Bab 6), kebutuhan di luar lingkup dan kendala (Bab 1/3/4/5). Opsional: file Bab 6 (atau bab lain) sebagai **pembanding kemiripan**.
- Skrip (bila ada pembanding): `analisis_teks.py kemiripan --teks bab7.txt --pembanding pembanding.txt` → kalimat mirip (komp. 3). Claude **tidak membaca** bab pembanding; hanya hasil skrip.
- Aturan khusus:
  - Buat **tabel penelusuran**: tiap kesimpulan → rumusan/tujuan yang dijawab → temuan di Bab 6; tiap saran → sumbernya (kebutuhan di luar lingkup / kendala / temuan evaluasi). Kesimpulan atau saran tanpa sumber → temuan ("kesimpulan baru"). Tanpa ringkasan dosen: "tidak dapat diverifikasi", jangan menebak asalnya.
  - Komp. 2: tabel per kesimpulan: ada konteks (siapa/apa/di mana)? ada bukti (metrik/jumlah)? berpotensi overclaim? Overclaim hanya **ditandai** untuk dosen.
  - Komp. 6: nilai tiga hal yang terlihat: saran sepele? fungsi standar? bernilai untuk penelitian lanjutan? Butir "sudah dituntut proposal" → "perlu diverifikasi dosen" (proposal tidak tersedia).
  - Bila **tidak ada saran**: lihat aturan umum bagian 3 (dosen memilih N/A atau 0). Saran yang ditujukan kepada pengguna program (bukan peneliti berikutnya) adalah kesalahan umum.

---
## Mode pendukung (Abstrak, Daftar Pustaka, Lampiran)
Rubrik: `rubrik-pendukung.md`, skor terpisah (P1 40, P2 30, P3 30). Perintah: `/periksa-bab pendukung`. Dosen dapat memilih satu atau ketiganya; tiap bagian pendek.
- **Abstrak (P1)**: `extract_bab.py --bagian abstrak` → `analisis_teks.py abstrak` (panjang, perkiraan melebihi setengah halaman) + render halaman untuk paragraf/spasi. Unsur isi (masalah, analisis dan desain, teknologi, evaluasi) dinilai Claude dari teksnya. Opsional kemiripan dengan Bab 1/6/7 (pembanding).
- **Daftar Pustaka (P2)**: `extract_bab.py <pdf> --teks-penuh /tmp/periksa/penuh.txt` dan `--bagian daftar-pustaka`; lalu `analisis_teks.py sitasi --naskah penuh.txt --pustaka daftar-pustaka.txt`. Skrip yang membaca seluruh naskah; Claude hanya membaca hasilnya dan halaman daftar pustaka untuk format APA. Hasil: sitasi tanpa entri, entri tak dikutip, urutan alfabet.
- **Lampiran (P3)**: `extract_bab.py --bagian lampiran` → `analisis_teks.py lampiran` (format halaman seperti "A-12", judul lampiran, user manual). Ikuti deskriptor apa adanya: user manual tidak ada = Level 1; catat kekurangan format di catatan.
- Jika PDF hanya berisi satu bab, bagian ini tidak ada: minta dosen mengunggah PDF lengkap atau halamannya.
