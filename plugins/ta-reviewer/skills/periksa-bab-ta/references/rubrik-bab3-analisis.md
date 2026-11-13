<!-- Rubrik Bab 3. Salinan bersih dari rubrik asli; isian kosong dan tanda tangan dibuang. Skor dihitung oleh scripts/hitung_skor.py -->

# Rubrik Penilaian Bab 3 (Analisis) Tugas Akhir
**Program Studi Teknik Informatika — Research Methodology**

> Sumber: slide kuliah *Chapter 3 – Analysis*. Poin bertanda **(slide)** berasal langsung dari slide. Poin bertanda **(pelengkap)** adalah indikator tambahan agar penilaian lebih operasional. Dosen dapat menyesuaikan bobot dan indikator pelengkap sesuai pedoman program studi.

## A. Konteks yang harus diketahui sebelum menilai

- Metode pengumpulan data yang dipakai: ☐ Survei/kuesioner ☐ Wawancara ☐ FGD ☐ Lainnya: ________

## B. Prinsip Dasar Bab 3 (dari slide)

Bab 3 terdiri dari **empat bagian** yang saling berurutan: **(slide)**

1. Analisis Keadaan Saat Ini (*Analysis of Current Conditions*)
2. Identifikasi Masalah (*Identification of Problem*)
3. Analisis Sistem Sejenis (*Benchmarking*)
4. Analisis Kebutuhan Sistem (*Analysis of System Requirements*)

Alur logisnya: kondisi saat ini → masalah → pembanding dari sistem sejenis → kebutuhan sistem. Masalah yang dibahas pada Identifikasi Masalah harus sudah dinyatakan pada Analisis Keadaan Saat Ini. **(slide)**

## C. Ringkasan Bobot

| No | Komponen | Bobot |
|---|---|---|
| 1 | Analisis Keadaan Saat Ini: Pengumpulan Data | 20 |
| 2 | Analisis Keadaan Saat Ini: Penyajian Data | 10 |
| 3 | Analisis Keadaan Saat Ini: Analisis Data | 15 |
| 4 | Identifikasi Masalah | 15 |
| 5 | Benchmarking (Analisis Sistem Sejenis) | 20 |
| 6 | Analisis Kebutuhan Sistem | 15 |
| 7 | Koherensi Alur Bab | 5 |
| | **Total** | **100** |

**Skala level:** 4 = Sangat Baik (100% bobot) · 3 = Baik (75%) · 2 = Cukup (50%) · 1 = Kurang (25%) · 0 = Tidak ada (0%)

**Rumus skor komponen:** `Skor = (Level / 4) × Bobot`

**Catatan tentang metode pengumpulan data:** Slide menguraikan lima fase survei. Slide juga menyebut survei dapat berupa wawancara, FGD, dan sebagainya. Jika mahasiswa memakai metode selain kuesioner, indikator yang khusus kuesioner (mis. rumus ukuran sampel, skala nominal/ordinal/interval) dapat dianggap N/A. Dosen menilai fase-fase yang setara untuk metode yang dipakai. Jika seluruh komponen tertentu N/A, hitung nilai akhir dengan `skor ÷ bobot yang berlaku × 100`.

## D. Rubrik Rinci per Komponen

### 1. Analisis Keadaan Saat Ini: Pengumpulan Data — Bobot 20

Survei digunakan untuk menggali informasi tentang **perilaku, sikap, karakteristik, harapan, dan pengetahuan** responden. **(slide)**

**Checklist indikator, mengikuti 5 fase survei (slide)**

*Fase 1 — Membangun instrumen*
- [ ] Hipotesis yang diuji teridentifikasi **(slide)**
- [ ] Jenis survei ditentukan (kuesioner, wawancara, FGD, dll.) **(slide)**
- [ ] Pertanyaan relevan dan mendukung hipotesis **(slide)**
- [ ] Kategori jawaban dinyatakan tepat (nominal, ordinal, interval) **(slide)**
- [ ] Tata letak instrumen dirancang **(slide)**
- [ ] Pertanyaan **bebas** dari jargon, ambiguitas, bahasa emosional, negasi ganda, dan pertanyaan yang mengarahkan (*leading*) **(slide)**

*Fase 2 — Menguji instrumen*
- [ ] Uji coba (*pilot test*) pada populasi kecil, untuk memeriksa **reliabilitas** (konsistensi hasil) dan kejelasan pertanyaan **(slide)**
- [ ] **Validitas** diperiksa melalui konsultasi dengan pakar, termasuk pertanyaan dan pilihan jawaban **(slide)**
- [ ] Sistem pencatatan data disiapkan: **anonimitas** responden dan **digitalisasi** hasil **(slide)**

*Fase 3 — Menentukan sampel*
- [ ] **Populasi target**, **kerangka sampel** (*sampling frame*), dan **ukuran sampel** dinyatakan jelas **(slide)**
- [ ] Ukuran sampel memadai: minimal 50 untuk kuesioner (30 adalah batas minimum mutlak) **(slide)**
- [ ] Rumus sesuai dipakai bila perlu: Cochran/Lemeshow untuk populasi tak diketahui (infinit), Slovin untuk populasi diketahui **(slide)**
- [ ] Sampel sesuai dengan masalah penelitian, bukan sampel yang tidak tepat **(slide: sampel tidak tepat menghasilkan hasil tidak akurat)**

*Fase 4 — Interaksi dengan responden*
- [ ] Materi pengumpulan data disiapkan **(slide)**
- [ ] Ada upaya meningkatkan tingkat respons (insentif, tindak lanjut lewat surat/telepon, pemilihan waktu) **(slide)**

*Fase 5 — Persiapan analisis (lihat juga komponen 3)*
- [ ] Data dimasukkan dan diperiksa ulang, termasuk data yang tidak lengkap **(slide)**

| Level | Deskriptor |
|---|---|
| **4** | Kelima fase terdokumentasi lengkap. Instrumen bebas dari kesalahan penyusunan, telah diuji reliabilitas dan validitasnya, sampel ditentukan dengan dasar yang jelas dan jumlahnya memadai. |
| **3** | Sebagian besar fase terdokumentasi. Ada kekurangan kecil (mis. uji validitas/reliabilitas kurang jelas, atau dasar penentuan sampel kurang kuat). |
| **2** | Hanya sebagian fase yang terdokumentasi. Instrumen belum diuji, atau sampel kecil/tanpa dasar penentuan. |
| **1** | Pengumpulan data tidak sistematis, instrumen bermasalah (pertanyaan mengarah/ambigu), atau sampel tidak sesuai. |
| **0** | Tidak ada pengumpulan data. |

---

### 2. Analisis Keadaan Saat Ini: Penyajian Data — Bobot 10

**Checklist indikator**
- [ ] Data disajikan **dengan tabel atau grafik yang tepat**, tidak hanya berupa teks **(slide: common mistake)**
- [ ] Jenis grafik sesuai sifat data: diagram lingkaran untuk proporsi dari keseluruhan, diagram garis untuk tren waktu, diagram batang untuk perbandingan antar kelompok **(slide)**
- [ ] **Garis dasar (*baseline*)** tidak dihilangkan. Jika sumbu dipotong (*truncated*), hal itu diberi tanda dan dijelaskan **(slide: tidak selalu salah, tetapi harus hati-hati)**
- [ ] Rentang sumbu Y wajar dan tidak melebih-lebihkan perbedaan **(slide)**
- [ ] Tidak memilih-milih data (*cherry picking*), seluruh data yang relevan ditampilkan **(slide)**
- [ ] Visualisasi mengikuti standar umum (mis. merah untuk bahaya, hijau untuk baik) **(slide)**
- [ ] Setiap grafik/tabel diberi judul, label, dan keterangan **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Seluruh data disajikan dalam tabel/grafik yang tepat jenisnya, jelas, dan tidak menyesatkan. |
| **3** | Penyajian umumnya tepat. Ada kekurangan kecil (mis. jenis grafik kurang ideal atau label kurang lengkap). |
| **2** | Sebagian data hanya berupa teks, atau terdapat penyajian yang berpotensi menyesatkan. |
| **1** | Data hanya berupa teks, atau grafik secara jelas menyesatkan (baseline hilang tanpa penjelasan, sumbu dimanipulasi, data dipilih-pilih). |
| **0** | Tidak ada penyajian data. |

---

### 3. Analisis Keadaan Saat Ini: Analisis Data — Bobot 15

Contoh pada slide (survei kantin) menunjukkan empat unsur analisis: **kedalaman**, **pemeriksaan silang**, **evaluasi**, dan **kesimpulan**. **(slide)**

**Checklist indikator**
- [ ] Analisis statistik dilakukan sesuai jenis data (mis. rata-rata, median, modus) **(slide)**
- [ ] **Kedalaman (*depth*):** data ditafsirkan, bukan hanya dilaporkan (mis. aspek mana yang kuat dan lemah dan mengapa) **(slide)**
- [ ] **Pemeriksaan silang (*cross examination*):** perbandingan antar kelompok responden atau variabel (mis. mahasiswa tahun pertama vs akhir) **(slide)**
- [ ] **Evaluasi:** menilai tingkat kondisi saat ini dan aspek yang paling lemah **(slide)**
- [ ] **Kesimpulan:** menyatakan tindak lanjut/prioritas yang muncul dari data **(slide)**
- [ ] Analisis **sesuai dengan tujuan** pengumpulan data **(slide: common mistake)**
- [ ] Data tidak hanya ditampilkan tanpa dianalisis **(slide: common mistake)**

| Level | Deskriptor |
|---|---|
| **4** | Data dianalisis mendalam, ada perbandingan antar kelompok/aspek, evaluasi, dan kesimpulan yang selaras dengan tujuan pengumpulan data. |
| **3** | Analisis cukup mendalam dan selaras dengan tujuan, tetapi salah satu unsur (pemeriksaan silang, evaluasi, atau kesimpulan) kurang kuat. |
| **2** | Analisis dangkal (hanya menyebut angka atau deskripsi), atau tidak sepenuhnya terkait dengan tujuan. |
| **1** | Data hanya ditampilkan tanpa analisis, atau analisis tidak berkaitan dengan tujuan. |
| **0** | Tidak ada analisis. |

---

### 4. Identifikasi Masalah — Bobot 15

Fungsi: dari analisis kondisi saat ini, mengidentifikasi masalah (aktual atau potensial) **secara rinci** dan membangun **hipotesis penyebab utamanya (*root cause*)**. Bila belum ada masalah yang muncul, dapat ditemukan **peluang** untuk mengembangkan sistem. **(slide)**

**Checklist indikator**
- [ ] Masalah diidentifikasi secara rinci dan spesifik **(slide)**
- [ ] Terdapat hipotesis akar penyebab masalah **(slide)**
- [ ] Masalah yang dibahas **sudah dinyatakan** dalam Analisis Keadaan Saat Ini (tidak muncul tiba-tiba) **(slide)**
- [ ] Masalah didukung oleh hasil analisis kondisi saat ini **dan** analisis sistem sejenis **(slide: common mistake)**
- [ ] Masalah relevan dengan rumusan masalah pada Bab 1 **(pelengkap)**
- [ ] Bila tidak ada masalah, peluang pengembangan dinyatakan dengan alasan **(slide)**

| Level | Deskriptor |
|---|---|
| **4** | Masalah rinci, jelas akar penyebabnya, seluruhnya berasal dari analisis kondisi saat ini dan sistem sejenis, serta selaras dengan Bab 1. |
| **3** | Masalah jelas dan didukung data, tetapi akar penyebab atau keterkaitan dengan analisis sistem sejenis kurang tegas. |
| **2** | Masalah bersifat umum, tanpa hipotesis akar penyebab, atau sebagian tidak didukung analisis sebelumnya. |
| **1** | Masalah tidak berasal dari analisis kondisi saat ini maupun sistem sejenis. |
| **0** | Komponen tidak ada. |

---

### 5. Benchmarking (Analisis Sistem Sejenis) — Bobot 20

Tujuan: mengamati kelebihan dan kekurangan sistem sejenis, lalu **mengikuti yang baik dan menghindari yang buruk**. **(slide)**

**Checklist indikator**
- [ ] Mengamati beberapa solusi/sistem lain yang tersedia dan relevan **(slide)**
- [ ] Kelebihan **dan** kekurangan setiap sistem dianalisis **(slide)**
- [ ] Kelebihan dan kekurangan **mengacu pada tinjauan pustaka atau identifikasi masalah**, bukan opini pribadi **(slide)**
- [ ] Analisis objektif berdasarkan teori atau kriteria yang jelas (mis. tabel perbandingan dengan kriteria) **(slide / pelengkap)**
- [ ] Tidak hanya membahas sisi buruk sistem **(slide: common mistake)**
- [ ] Kriteria perbandingan sesuai dengan masalah yang diidentifikasi **(pelengkap)**
- [ ] Hasil perbandingan menunjukkan celah yang belum terjawab sistem lain **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Beberapa sistem sejenis dibandingkan secara objektif berdasarkan kriteria yang berlandaskan teori/masalah. Kelebihan dan kekurangan seimbang, dan celah yang belum terjawab terlihat jelas. |
| **3** | Perbandingan objektif dan memuat kelebihan serta kekurangan, tetapi kriteria atau keterkaitan dengan masalah kurang tegas. |
| **2** | Perbandingan sebagian bersifat deskriptif atau subjektif, atau hanya sedikit sistem yang dibahas. |
| **1** | Analisis berdasarkan pilihan pribadi, atau hanya membahas kekurangan sistem. |
| **0** | Komponen tidak ada. |

---

### 6. Analisis Kebutuhan Sistem — Bobot 15

Fungsi: **hipotesis tentang bagaimana sistem yang diusulkan perlu dibangun**, berdasarkan seluruh analisis sebelumnya. **(slide)**

**Checklist indikator**
- [ ] **Mengadaptasi kelebihan** sistem sejenis yang dianggap solusi dari masalah saat ini **(slide)**
- [ ] **Menghindari kekurangan** sistem sejenis agar tidak mengulang kesalahan yang sama **(slide)**
- [ ] Mencari solusi atas masalah yang **belum teratasi** oleh sistem lain **(slide)**
- [ ] Setiap kebutuhan **terhubung dengan identifikasi masalah** **(slide: common mistake)**
- [ ] Kebutuhan dirumuskan jelas dan dapat diverifikasi (mis. fungsional dan non-fungsional) **(pelengkap)**
- [ ] Tidak ada kebutuhan yang muncul tanpa dasar analisis **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Setiap kebutuhan dapat ditelusuri ke masalah dan hasil benchmarking. Memuat adaptasi kelebihan, penghindaran kekurangan, dan solusi atas celah yang ada. |
| **3** | Kebutuhan sebagian besar terhubung dengan masalah dan benchmarking. Ada sebagian yang kurang beralasan. |
| **2** | Kebutuhan berupa daftar umum dengan keterkaitan lemah terhadap masalah. |
| **1** | Kebutuhan tidak berkaitan dengan identifikasi masalah. |
| **0** | Komponen tidak ada. |

---

### 7. Koherensi Alur Bab — Bobot 5

**Checklist indikator** (seluruhnya **pelengkap**)
- [ ] Urutan bagian sesuai: kondisi saat ini → masalah → benchmarking → kebutuhan
- [ ] Bab selaras dengan rumusan masalah dan tujuan di Bab 1, serta menggunakan teori dari Bab 2
- [ ] Bahasa baku, sitasi konsisten, dan format sesuai pedoman
- [ ] Gambar/tabel bernomor dan dirujuk dalam teks

| Level | Deskriptor |
|---|---|
| **4** | Alur sangat runtut dan selaras dengan Bab 1 dan 2. Bahasa dan format konsisten. |
| **3** | Alur runtut, dengan sedikit kesalahan bahasa/format. |
| **2** | Alur kurang runtut atau kesalahan bahasa/format cukup banyak. |
| **1** | Alur terputus dan mengganggu pemahaman. |
| **0** | Tidak memenuhi standar. |

## E. Pemeriksaan Kesalahan Umum (*Common Mistakes*)

Dari slide. Centang bila **ditemukan**.

| ☐ | Temuan | Dampak penilaian |
|---|---|---|
| ☐ | Data survei dan sejenisnya hanya disajikan dalam teks, tanpa tabel/grafik yang jelas | Komponen 2 |
| ☐ | Data disajikan secara menyesatkan (baseline hilang, sumbu Y dimanipulasi, *cherry picking*, jenis grafik/visualisasi tidak tepat) | Komponen 2 |
| ☐ | Data hanya disajikan dan tidak dianalisis sama sekali | Komponen 3 |
| ☐ | Data tidak dianalisis sesuai tujuan | Komponen 3 |
| ☐ | Identifikasi masalah tidak mengacu pada analisis kondisi saat ini dan sistem sejenis | Komponen 4 |
| ☐ | Analisis sistem sejenis bersifat subjektif (pilihan pribadi), bukan berdasarkan teori atau identifikasi masalah | Komponen 5 |
| ☐ | Analisis sistem sejenis hanya membahas sisi buruknya | Komponen 5 |
| ☐ | Analisis kebutuhan sistem tidak terkait dengan identifikasi masalah | Komponen 6 |

## F. Pemeriksaan Konsistensi Silang (cepat)

- [ ] Setiap masalah pada Identifikasi Masalah **dapat ditelusuri** ke data/analisis kondisi saat ini
- [ ] Kriteria benchmarking berhubungan dengan masalah yang diidentifikasi
- [ ] Setiap kebutuhan sistem **berasal dari** masalah atau hasil benchmarking
- [ ] Masalah dan kebutuhan sejalan dengan **rumusan masalah dan tujuan** di Bab 1
- [ ] Kebutuhan sistem dapat dipenuhi oleh solusi yang dibahas pada bab perancangan berikutnya

## G. Interpretasi skor

| Rentang | Kategori | Keputusan |
|---|---|---|
| 85–100 | Sangat Baik | Layak, revisi minimal |
| 70–84 | Baik | Layak dengan revisi ringan |
| 55–69 | Cukup | Perlu revisi signifikan |
| < 55 | Kurang | Belum layak, susun ulang bagian utama |
