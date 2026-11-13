<!-- Rubrik Bab 6. Salinan bersih dari rubrik asli; isian kosong dan tanda tangan dibuang. Skor dihitung oleh scripts/hitung_skor.py -->

# Rubrik Penilaian Bab 6 (Evaluasi) Tugas Akhir
**Program Studi Teknik Informatika — Research Methodology**

> Sumber: slide kuliah *Chapter 6 – Evaluation*, termasuk catatan pembicara (*notes*). Poin bertanda **(slide)** berasal langsung dari slide. Poin bertanda **(pelengkap)** adalah indikator tambahan agar penilaian lebih operasional. Dosen dapat menyesuaikan bobot dan indikator pelengkap sesuai pedoman program studi.

## A. Konteks yang harus diketahui sebelum menilai

- Jenis topik penelitian: ☐ Aplikasi/Sistem Informasi ☐ Game ☐ Multimedia ☐ AI/ML ☐ Lainnya: ________

## B. Prinsip Dasar Bab 6 (dari slide)

Bab Evaluasi terdiri dari dua bagian yang **berbeda**: **Verifikasi** dan **Validasi**. **(slide)**

| | Verifikasi | Validasi |
|---|---|---|
| **Pelaku** | Programmer (pengembang) | Target pasar / pengguna |
| **Peran** | *Quality Assurance* | Pengguna |
| **Proses** | Pelaku menguji program menggunakan sekumpulan data | Sekelompok pengguna mencoba aplikasi dengan skenario tertentu. Hasil diamati, atau tanggapan diperiksa melalui tes, survei, wawancara, dll. |

Prinsip tambahan:
1. **Verifikasi** (aplikasi/sistem informasi): menguji program berdasarkan skenario yang menggunakan **seluruh fitur** secara berurutan, misalnya mulai dari menambah data, transaksi, hingga laporan. **(slide)**
2. **Verifikasi** (game): menguji berdasarkan skenario yang menunjukkan proses penting, misalnya pembuatan pengguna baru, memulai game, naik level, akhir game. **(slide)**
3. **Validasi:** meminta pengguna menjalankan skenario (mis. membeli sesuatu di toko elektronik) atau memainkan game, lalu mengamati atau melakukan survei/wawancara tentang pengalaman dan hasilnya. **Wajib memeriksa apakah tujuan penelitian tercapai.** **(slide)**
4. Uji verifikasi cukup mewakili keseluruhan sistem. **Tidak perlu semua sistem diverifikasi**, terutama bagian yang berulang. **(slide, notes)**

## C. Ringkasan Bobot

| No | Komponen | Bobot |
|---|---|---|
| 1 | Struktur Bab dan Pemisahan Verifikasi vs Validasi | 5 |
| 2 | Perancangan dan Cakupan Verifikasi | 20 |
| 3 | Penulisan Verifikasi (bukan manual pengguna, kegagalan ditampilkan) | 10 |
| 4 | Perancangan Validasi (skenario dan partisipan) | 15 |
| 5 | Ketepatan Instrumen Validasi | 15 |
| 6 | Analisis dan Evaluasi Hasil Validasi | 15 |
| 7 | Keterkaitan dengan Masalah dan Pencapaian Tujuan Penelitian | 15 |
| 8 | Koherensi, Bahasa, dan Format | 5 |
| | **Total** | **100** |

**Skala level:** 4 = Sangat Baik (100% bobot) · 3 = Baik (75%) · 2 = Cukup (50%) · 1 = Kurang (25%) · 0 = Tidak ada (0%)

**Rumus skor komponen:** `Skor = (Level / 4) × Bobot`

**Komponen yang tidak berlaku (N/A):** Bila suatu indikator memang tidak relevan dengan topik, jangan beri nilai 0. Hitung nilai akhir dengan `skor ÷ bobot yang berlaku × 100`.

## D. Rubrik Rinci per Komponen

### 1. Struktur Bab dan Pemisahan Verifikasi vs Validasi — Bobot 5

**Checklist indikator**
- [ ] Bab memuat **dua subbab terpisah**: Verifikasi dan Validasi **(slide)**
- [ ] Judul subbab **benar**: bukan "6.1 Uji Coba" dan "6.2 Evaluasi" **(slide: common mistake)**
- [ ] Pelaku, peran, dan proses masing-masing dibedakan dengan jelas (verifikasi oleh pengembang, validasi oleh pengguna) **(slide)**
- [ ] Pengantar bab menjelaskan perbedaan keduanya secara singkat **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Dua subbab berjudul tepat, dengan perbedaan pelaku, peran, dan proses yang jelas. |
| **3** | Dua subbab terpisah dan berjudul tepat, tetapi pembedaan kurang dijelaskan. |
| **2** | Judul subbab salah, atau pembedaan keduanya kabur. |
| **1** | Verifikasi dan validasi bercampur dalam satu uraian. |
| **0** | Salah satu tidak ada. |

---

### 2. Perancangan dan Cakupan Verifikasi — Bobot 20

**Checklist indikator**
- [ ] Pelaku verifikasi adalah pengembang sebagai *quality assurance* **(slide)**
- [ ] Pengujian menggunakan **sekumpulan data** yang disebutkan jelas **(slide)**
- [ ] **Aplikasi/Sistem Informasi:** skenario mencakup seluruh fitur secara berurutan (mis. tambah data → transaksi → laporan) **(slide)**
- [ ] **Game:** skenario mencakup proses penting (pengguna baru, memulai game, naik level, akhir game, dll.) **(slide)**
- [ ] **AI/lainnya:** pengujian sesuai karakter topik, dengan data uji dan metrik yang jelas **(pelengkap)**
- [ ] Skenario **representatif**. Bagian yang berulang tidak diuji satu per satu **(slide, notes)**
- [ ] Hasil pengujian dilaporkan jelas (lulus/gagal, nilai metrik) dan sesuai dengan kebutuhan sistem di Bab 3 **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Skenario dan data uji jelas, mewakili seluruh fitur/proses penting, tanpa pengujian berulang yang tidak perlu. Hasil terlapor jelas dan terkait kebutuhan sistem. |
| **3** | Skenario mencakup hampir seluruh fitur penting. Sedikit kekurangan dalam data uji atau pelaporan hasil. |
| **2** | Skenario hanya mencakup sebagian fitur penting, atau terlalu rinci pada bagian berulang. |
| **1** | Pengujian tidak sistematis atau tidak mewakili sistem. |
| **0** | Tidak ada verifikasi. |

---

### 3. Penulisan Verifikasi — Bobot 10

**Checklist indikator**
- [ ] Verifikasi **tidak** ditulis seperti **buku panduan pengguna** (*user manual*) **(slide: common mistake)**
- [ ] **Verifikasi atas metode yang gagal** juga ditampilkan **(slide: common mistake)**
- [ ] Kegagalan dilengkapi analisis penyebab dan tindak lanjutnya **(pelengkap)**
- [ ] Penulisan berorientasi pada pengujian (skenario, masukan, hasil yang diharapkan, hasil aktual), bukan langkah penggunaan fitur **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Ditulis sebagai pengujian yang sistematis. Hasil sukses dan gagal ditampilkan jujur, dengan analisis dan tindak lanjut. |
| **3** | Berorientasi pengujian. Kegagalan disebut tetapi analisisnya kurang. |
| **2** | Sebagian bernuansa manual pengguna, atau kegagalan hampir tidak ditampilkan. |
| **1** | Ditulis seluruhnya seperti manual pengguna, dan hanya hasil sukses yang ditampilkan. |
| **0** | Tidak ada. |

---

### 4. Perancangan Validasi (Skenario dan Partisipan) — Bobot 15

**Checklist indikator**
- [ ] Partisipan adalah **target pasar/pengguna sasaran**, bukan pengembang **(slide)**
- [ ] Pengguna menjalankan **skenario tertentu** dengan tugas yang jelas (mis. membeli barang di toko elektronik, memainkan game) **(slide)**
- [ ] Hasil **diamati**, atau tanggapan diperiksa melalui **tes, survei, wawancara**, dsb. **(slide)**
- [ ] Jumlah dan karakteristik partisipan dijelaskan dan memadai **(pelengkap)**
- [ ] Prosedur validasi (pengantar, tugas, pengumpulan data) terdokumentasi **(pelengkap)**
- [ ] Hal etis diperhatikan (persetujuan partisipan, anonimitas) **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Partisipan sesuai target pasar dan jumlahnya memadai. Skenario, prosedur, dan cara pengumpulan data jelas dan terdokumentasi. |
| **3** | Partisipan dan skenario sesuai, tetapi ada kekurangan pada jumlah atau dokumentasi prosedur. |
| **2** | Partisipan kurang mewakili target pasar, atau skenario terlalu umum. |
| **1** | Validasi dilakukan oleh pengembang atau pihak yang tidak sesuai, tanpa skenario yang jelas. |
| **0** | Tidak ada validasi. |

---

### 5. Ketepatan Instrumen Validasi — Bobot 15

**Checklist indikator**
- [ ] Instrumen **sesuai dengan apa yang ingin diukur** **(slide: common mistake)**
- [ ] Untuk klaim *pembelajaran*: memakai **kuis/tes pemahaman**, bukan sekadar menanyakan apakah aplikasi membantu belajar **(slide, contoh)**
- [ ] Untuk klaim *UX membantu pekerjaan*: **mengamati perilaku pengguna** saat mengerjakan tugas atau **mengukur waktu penyelesaian**, bukan sekadar bertanya apakah UX membantu **(slide, contoh)**
- [ ] Ukuran objektif (perilaku, waktu, skor) digunakan di samping persepsi/opini bila perlu **(pelengkap)**
- [ ] Instrumen (kuesioner, panduan wawancara, kuis) dicantumkan atau dijelaskan **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Instrumen tepat dan langsung mengukur klaim penelitian, dengan kombinasi ukuran objektif dan persepsi bila sesuai. |
| **3** | Instrumen umumnya tepat. Sebagian hanya mengandalkan persepsi pengguna. |
| **2** | Instrumen kurang sesuai (mis. hanya menanyakan "apakah membantu"), atau tidak dijelaskan. |
| **1** | Instrumen keliru dan tidak mengukur klaim penelitian. |
| **0** | Tidak ada instrumen. |

---

### 6. Analisis dan Evaluasi Hasil Validasi — Bobot 15

**Checklist indikator**
- [ ] Hasil survei/wawancara/tes **tidak hanya ditampilkan apa adanya**, tetapi **dianalisis dan dievaluasi** **(slide: common mistake)**
- [ ] Data disajikan dengan tabel/grafik yang jelas dan tidak menyesatkan **(pelengkap, mengacu Bab 3)**
- [ ] Analisis mencakup tafsiran, perbandingan antar kelompok/aspek, dan kesimpulan **(pelengkap)**
- [ ] Temuan negatif atau hasil di luar dugaan dibahas **(pelengkap)**
- [ ] Keterbatasan validasi disebutkan **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Hasil dianalisis mendalam dan dievaluasi, termasuk temuan negatif. Kesimpulan didukung data dan keterbatasan diakui. |
| **3** | Analisis cukup baik, tetapi tafsiran atau pembahasan temuan negatif kurang. |
| **2** | Analisis dangkal, sebagian hanya mendeskripsikan angka. |
| **1** | Hasil hanya ditampilkan apa adanya tanpa analisis. |
| **0** | Tidak ada analisis. |

---

### 7. Keterkaitan dengan Masalah dan Pencapaian Tujuan Penelitian — Bobot 15

**Checklist indikator**
- [ ] Validasi **memeriksa apakah tujuan penelitian tercapai** **(slide)**
- [ ] Validasi berfokus pada **penyelesaian masalah** pada rumusan masalah, **bukan hanya UI/UX** **(slide: common mistake)**
- [ ] Ada **hubungan antara analisis (Bab 3) dan validasi**, misalnya masalah dan kebutuhan yang diidentifikasi diuji kembali **(slide: common mistake)**
- [ ] Setiap rumusan masalah dan tujuan di Bab 1 dapat ditelusuri ke bukti di bab ini **(pelengkap)**
- [ ] Kesimpulan tentang pencapaian tujuan jelas (tercapai, sebagian, atau tidak) **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Setiap tujuan dan masalah penelitian diuji dengan bukti yang jelas. Hubungan dengan analisis di Bab 3 tegas, dan pencapaian tujuan dinyatakan eksplisit. |
| **3** | Sebagian besar tujuan terjawab. Hubungan dengan analisis ada tetapi kurang tegas. |
| **2** | Validasi hanya sebagian terkait masalah. Banyak berfokus pada aspek tampilan atau kepuasan umum. |
| **1** | Validasi hanya UI/UX dan tidak terkait masalah maupun hasil analisis. |
| **0** | Tidak ada keterkaitan. |

---

### 8. Koherensi, Bahasa, dan Format — Bobot 5

**Checklist indikator** (seluruhnya **pelengkap**)
- [ ] Alur bab runtut: verifikasi → validasi → analisis
- [ ] Tabel/grafik/gambar bernomor, berjudul, dan dirujuk dalam teks
- [ ] Bahasa baku dan istilah konsisten dengan Bab 1–5
- [ ] Kutipan dan referensi metode evaluasi konsisten

| Level | Deskriptor |
|---|---|
| **4** | Alur runtut, tabel dan grafik terbaca dan dirujuk, bahasa dan format konsisten. |
| **3** | Alur runtut dengan sedikit kesalahan bahasa/format. |
| **2** | Alur kurang runtut atau banyak kesalahan format. |
| **1** | Alur terputus dan mengganggu pemahaman. |
| **0** | Tidak memenuhi standar. |

## E. Pemeriksaan Kesalahan Umum (*Common Mistakes*)

Dari slide. Centang bila **ditemukan**.

| ☐ | Temuan | Dampak penilaian |
|---|---|---|
| ☐ | Verifikasi ditulis seperti manual pengguna | Komponen 3 |
| ☐ | Verifikasi atas metode yang gagal tidak ditampilkan | Komponen 3 |
| ☐ | Judul subbab salah (mis. 6.1 Uji Coba, 6.2 Evaluasi) | Komponen 1 |
| ☐ | Validasi hanya pada UI/UX, tidak berfokus pada penyelesaian masalah | Komponen 7 |
| ☐ | Tidak ada hubungan antara analisis dan validasi | Komponen 7 |
| ☐ | Instrumen validasi salah (mis. hanya bertanya "apakah membantu belajar", bukan kuis; hanya bertanya "apakah UX membantu", bukan mengamati perilaku atau mengukur waktu) | Komponen 5 |
| ☐ | Hasil validasi (survei/wawancara) hanya ditampilkan apa adanya tanpa analisis dan evaluasi | Komponen 6 |

## F. Pemeriksaan Konsistensi Silang (cepat)

- [ ] Setiap **kebutuhan sistem** di Bab 3 diuji pada verifikasi atau validasi
- [ ] Setiap **rumusan masalah dan tujuan** di Bab 1 memiliki bukti pada bab ini
- [ ] Fitur/proses yang diverifikasi sesuai dengan yang diimplementasikan di **Bab 5**
- [ ] Hipotesis di analisis (Bab 3) diperiksa kembali dalam validasi
- [ ] Kesimpulan (bab berikutnya) hanya mengklaim yang didukung hasil evaluasi

## G. Interpretasi skor

| Rentang | Kategori | Keputusan |
|---|---|---|
| 85–100 | Sangat Baik | Layak, revisi minimal |
| 70–84 | Baik | Layak dengan revisi ringan |
| 55–69 | Cukup | Perlu revisi signifikan |
| < 55 | Kurang | Belum layak, susun ulang bagian utama |
