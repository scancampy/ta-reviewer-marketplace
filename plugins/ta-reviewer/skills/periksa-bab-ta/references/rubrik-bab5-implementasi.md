<!-- Rubrik Bab 5. Salinan bersih dari rubrik asli; isian kosong dan tanda tangan dibuang. Skor dihitung oleh scripts/hitung_skor.py -->

# Rubrik Penilaian Bab 5 (Implementasi) Tugas Akhir
**Program Studi Teknik Informatika — Research Methodology**

> Sumber: slide kuliah *Chapter 5 – Implementation*, termasuk catatan pembicara (*notes*) pada slide. Poin bertanda **(slide)** berasal langsung dari slide. Poin bertanda **(pelengkap)** adalah indikator tambahan agar penilaian lebih operasional. Dosen dapat menyesuaikan bobot dan indikator pelengkap sesuai pedoman program studi.

## A. Konteks yang harus diketahui sebelum menilai

- Jenis topik penelitian: ☐ Sistem Informasi ☐ Multimedia ☐ AI/ML ☐ Game ☐ Sistem Pakar ☐ Lainnya: ________

## B. Prinsip Dasar Bab 5 (dari slide)

1. Prinsip utama: **PROCESS over RESULT**. Bab ini menjawab **"bagaimana proses implementasinya?"**, bukan "apa hasilnya?". **(slide)**
2. Yang diceritakan adalah **bagaimana membuatnya**, bukan bagaimana hasilnya. **(slide, notes)**
3. Jangan menampilkan hasil implementasi. Tampilkan **proses di balik layar**: implementasi UI/UX, basis data, proses (kode), fase dan *pipeline*, dan mekanisme lain. **(slide)**
4. Bab ini **berkaitan erat dengan Bab 4 (Desain)**. Setiap desain diikuti penjelasan cara mengimplementasikannya. **(slide)**
5. Hanya bagian **penting dan menantang** yang dijelaskan. Bagian paling krusial dari penelitian wajib ada. Kode sederhana yang umum (mis. proses login sederhana) tidak perlu dijelaskan. **(slide)**
6. **Kegagalan** boleh dan penting untuk didokumentasikan, dengan penjelasan teknis dan cara mengatasinya. **(slide)**

## C. Ringkasan Bobot

| No | Komponen | Bobot |
|---|---|---|
| 1 | Fokus pada Proses, Bukan Hasil | 20 |
| 2 | Keterkaitan dengan Desain (Bab 4) | 15 |
| 3 | Seleksi Bagian Penting dan Menantang | 10 |
| 4 | Penjelasan Kode/Mekanisme Implementasi | 20 |
| 5 | Dokumentasi Kegagalan dan Hambatan | 15 |
| 6 | Gaya Penulisan (narasi teknis, bukan tutorial) | 5 |
| 7 | Kelengkapan Dokumentasi Proses sesuai Topik | 10 |
| 8 | Koherensi, Bahasa, dan Format | 5 |
| | **Total** | **100** |

**Skala level:** 4 = Sangat Baik (100% bobot) · 3 = Baik (75%) · 2 = Cukup (50%) · 1 = Kurang (25%) · 0 = Tidak ada (0%)

**Rumus skor komponen:** `Skor = (Level / 4) × Bobot`

**Komponen yang tidak berlaku (N/A):** Bila suatu indikator memang tidak relevan dengan topik (mis. dokumentasi *shooting* dan *dubbing* untuk penelitian non-multimedia), jangan beri nilai 0. Hitung nilai akhir dengan `skor ÷ bobot yang berlaku × 100`.

## D. Rubrik Rinci per Komponen

### 1. Fokus pada Proses, Bukan Hasil — Bobot 20

**Checklist indikator**
- [ ] Bab menjelaskan **bagaimana** implementasi dilakukan (langkah, keputusan teknis, mekanisme) **(slide)**
- [ ] **Tidak** didominasi tangkapan layar hasil aplikasi **(slide)**
- [ ] Setiap gambar hasil, bila ada, disertai penjelasan proses di baliknya, bukan sekadar "melapor bahwa aplikasi telah jadi" **(slide, notes)**
- [ ] Tampilan hasil akhir yang menyeluruh dialihkan ke bab Pengujian/Hasil **(pelengkap)**
- [ ] Yang ditampilkan adalah proses di balik layar: UI/UX, basis data, kode proses, fase dan *pipeline*, mekanisme lain **(slide)**

| Level | Deskriptor |
|---|---|
| **4** | Seluruh bab berfokus pada proses. Gambar hasil hanya sebagai pendukung dan selalu disertai penjelasan cara pembuatannya. |
| **3** | Sebagian besar berfokus pada proses. Ada beberapa tangkapan layar hasil dengan penjelasan proses yang minim. |
| **2** | Proporsi hasil dan proses seimbang. Banyak gambar hasil tanpa penjelasan proses. |
| **1** | Bab terutama berisi tangkapan layar hasil aplikasi dengan sedikit penjelasan proses. |
| **0** | Hanya hasil, tidak ada proses. |

---

### 2. Keterkaitan dengan Desain (Bab 4) — Bobot 15

**Checklist indikator**
- [ ] Bab ini **terhubung kuat** dengan Bab 4 **(slide)**
- [ ] Setiap bagian desain penting memiliki padanan implementasi: desain aset → implementasi aset, desain data → implementasi data, dst. **(slide, notes)**
- [ ] Implementasi mengikuti desain. Penyimpangan dari desain dinyatakan dan dijelaskan alasannya **(pelengkap)**
- [ ] Urutan bagian sejalan dengan urutan di Bab 4 **(pelengkap)**
- [ ] Tidak ada fitur yang diimplementasikan tanpa dasar desain **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Setiap bagian desain penting memiliki padanan implementasi yang jelas. Penyimpangan dijelaskan. |
| **3** | Hampir seluruh desain memiliki padanan. Sebagian keterkaitan hanya tersirat. |
| **2** | Beberapa bagian desain tidak diimplementasikan, atau implementasi tidak sesuai desain tanpa penjelasan. |
| **1** | Implementasi hampir tidak berkaitan dengan desain. |
| **0** | Tidak ada keterkaitan. |

---

### 3. Seleksi Bagian Penting dan Menantang — Bobot 10

**Checklist indikator**
- [ ] **Bagian paling krusial** dari penelitian (inti kontribusi) terdokumentasi **(slide)**
- [ ] Bagian yang **sulit dan *tricky*** dijelaskan **(slide, notes)**
- [ ] Kode sederhana dan umum (mis. login sederhana, CRUD biasa) **tidak** dijelaskan **(slide)**
- [ ] Tidak semua kode ditampilkan dan dijelaskan **(slide, notes)**
- [ ] Alasan suatu bagian dianggap penting/menantang dapat dipahami **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Hanya bagian krusial dan menantang yang diuraikan. Seluruh inti penelitian tercakup. Bagian sepele dihilangkan. |
| **3** | Bagian krusial tercakup, dengan sedikit uraian bagian sepele. |
| **2** | Campuran antara bagian penting dan sepele, atau satu bagian inti terlewat. |
| **1** | Mayoritas uraian tentang bagian sepele, sementara inti penelitian tidak dibahas. |
| **0** | Tidak ada seleksi, atau tidak ada bagian krusial yang dibahas. |

---

### 4. Penjelasan Kode/Mekanisme Implementasi — Bobot 20

**Checklist indikator**
- [ ] **Setiap kode** yang ditampilkan **dijelaskan**, dan penjelasannya **lebih panjang** daripada kodenya (mis. 10 baris kode dijelaskan minimal 10 baris atau lebih) **(slide)**
- [ ] Kode **tidak** ditampilkan tanpa penjelasan, atau hanya dijelaskan lewat komentar internal (mis. `// ...` pada C++ atau C#) **(slide: common mistake)**
- [ ] Kode serupa **tidak diulang** dan **tidak disalin-tempel** dari bagian lain. Cukup disebutkan bahwa bagian itu sudah dibahas **(slide)**
- [ ] Penjelasan mencakup logika, alasan teknis, dan hubungannya dengan desain, bukan hanya membaca kode baris demi baris **(pelengkap)**
- [ ] Untuk topik AI/pipeline: fase dan alur diuraikan, dan parameter penting beserta alasan pemilihannya dijelaskan **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Seluruh kode terpilih dijelaskan dengan penjelasan lebih panjang daripada kodenya. Logika dan alasan teknis jelas. Tidak ada pengulangan. |
| **3** | Sebagian besar kode dijelaskan memadai. Beberapa penjelasan singkat atau ada pengulangan kecil. |
| **2** | Penjelasan umumnya hanya menyebut fungsi kode secara garis besar, atau sebagian kode tanpa penjelasan. |
| **1** | Kode ditampilkan tanpa penjelasan atau hanya dengan komentar internal. |
| **0** | Tidak ada penjelasan. |

---

### 5. Dokumentasi Kegagalan dan Hambatan — Bobot 15

**Checklist indikator**
- [ ] Kegagalan/hambatan implementasi **didokumentasikan** (bukan hanya yang berhasil) **(slide)**
- [ ] Kegagalan ditunjukkan **secara rinci**, disertai **penjelasan teknis** dan **cara mengatasinya** **(slide)**
- [ ] Bila hasil penelitian tidak sesuai hipotesis awal, hal itu **dijelaskan dan dievaluasi dengan layak** **(slide)**
- [ ] Pembelajaran dari kegagalan terlihat (apa yang berubah akibat kegagalan) **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Kegagalan penting dipaparkan rinci dengan sebab teknis, solusi, dan pelajaran. Hasil yang tidak sesuai hipotesis dievaluasi dengan baik. |
| **3** | Kegagalan dipaparkan dengan sebab dan solusi, tetapi kurang rinci atau tanpa evaluasi mendalam. |
| **2** | Kegagalan hanya disebut sekilas tanpa penjelasan teknis atau solusi. |
| **1** | Hanya implementasi yang berhasil yang ditulis. Tidak ada hambatan sama sekali yang disebut, padahal prosesnya wajar menghadapi hambatan. |
| **0** | Tidak ada, dan bab terkesan mengabaikan masalah yang jelas terjadi. |
| **N/A** | Hanya dipakai bila dosen yakin tidak ada hambatan berarti selama implementasi. |

---

### 6. Gaya Penulisan (Narasi Teknis, Bukan Tutorial) — Bobot 5

**Checklist indikator**
- [ ] Ditulis seperti **menceritakan kembali proses dengan penjelasan teknis yang terstruktur** **(slide, notes)**
- [ ] **Bukan** gaya tutorial langkah demi langkah (mis. "klik menu ..., lalu pilih ...") **(slide: common mistake)**
- [ ] Menggunakan bahasa deskriptif dan istilah teknis yang tepat **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Narasi teknis terstruktur dan mengalir. Tidak ada kesan tutorial. |
| **3** | Umumnya narasi teknis. Sesekali bernuansa tutorial. |
| **2** | Banyak bagian berupa langkah-langkah ala tutorial. |
| **1** | Seluruh bab ditulis sebagai tutorial langkah demi langkah. |
| **0** | Tidak dapat dinilai. |

---

### 7. Kelengkapan Dokumentasi Proses sesuai Topik — Bobot 10

**Checklist indikator**
- [ ] Mekanisme implementasi yang relevan terdokumentasi: UI/UX, basis data, proses (kode), fase dan *pipeline*, mekanisme lain **(slide)**
- [ ] **Multimedia:** proses produksi (mis. *shooting*, *dubbing*, *foley*) terdokumentasi, bukan hanya hasil akhirnya **(slide: common mistake)**
- [ ] **AI/ML:** alur *pipeline* (data, pra-pemrosesan, pelatihan, dsb.) terdokumentasi **(pelengkap)**
- [ ] **Game:** implementasi gameplay dan aset terdokumentasi **(pelengkap)**
- [ ] Bukti pendukung proses tersedia (tangkapan layar proses, log, cuplikan konfigurasi) bila relevan **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Seluruh proses yang relevan dengan topik terdokumentasi lengkap dan terstruktur. |
| **3** | Hampir seluruh proses terdokumentasi. Satu aspek kurang lengkap. |
| **2** | Beberapa proses penting tidak terdokumentasi. |
| **1** | Hanya sebagian kecil proses yang terdokumentasi. |
| **0** | Tidak ada dokumentasi proses. |
| **N/A** | Indikator topik tertentu tidak berlaku (dinilai dari indikator lain). |

---

### 8. Koherensi, Bahasa, dan Format — Bobot 5

**Checklist indikator** (seluruhnya **pelengkap**)
- [ ] Alur bab runtut dan logis
- [ ] Gambar dan listing kode bernomor, berjudul, dan dirujuk dalam teks
- [ ] Kode dapat dibaca (pemformatan rapi, tidak terpotong)
- [ ] Bahasa baku dan istilah konsisten dengan Bab 1–4

| Level | Deskriptor |
|---|---|
| **4** | Alur runtut. Gambar dan listing dirujuk dan terbaca. Bahasa dan format konsisten. |
| **3** | Alur runtut dengan sedikit kesalahan bahasa/format. |
| **2** | Alur kurang runtut atau listing sulit dibaca. |
| **1** | Alur terputus dan mengganggu pemahaman. |
| **0** | Tidak memenuhi standar. |

## E. Pemeriksaan Kesalahan Umum (*Common Mistakes*)

Dari slide. Centang bila **ditemukan**.

| ☐ | Temuan | Dampak penilaian |
|---|---|---|
| ☐ | Hanya menampilkan hasil (biasanya tangkapan layar UI), bukan proses implementasi | Komponen 1 |
| ☐ | Menampilkan kode tanpa penjelasan, atau hanya dengan komentar internal | Komponen 4 |
| ☐ | Penjelasan kode lebih pendek daripada kodenya | Komponen 4 |
| ☐ | Kode serupa diulang atau disalin-tempel dari bagian lain | Komponen 4 |
| ☐ | Menjelaskan bagian sepele yang umum (mis. login sederhana) | Komponen 3 |
| ☐ | Mahasiswa multimedia lupa mendokumentasikan proses (*shooting*, *dubbing*, *foley*, dsb.) sehingga harus mengulang | Komponen 7 |
| ☐ | Hambatan dan kegagalan implementasi tidak pernah disebut | Komponen 5 |
| ☐ | Bab ditulis sebagai tutorial langkah demi langkah | Komponen 6 |

## F. Pemeriksaan Konsistensi Silang (cepat)

- [ ] Setiap bagian desain penting di **Bab 4** memiliki padanan implementasi di bab ini
- [ ] Implementasi memenuhi **kebutuhan sistem** di Bab 3
- [ ] Teknologi, metode, atau algoritma yang dipakai sesuai dengan **landasan teori** di Bab 2
- [ ] Penyimpangan dari desain telah dijelaskan alasannya
- [ ] Hasil akhir yang tidak dimuat di sini dibahas di bab **Pengujian/Hasil**

## G. Interpretasi skor

| Rentang | Kategori | Keputusan |
|---|---|---|
| 85–100 | Sangat Baik | Layak, revisi minimal |
| 70–84 | Baik | Layak dengan revisi ringan |
| 55–69 | Cukup | Perlu revisi signifikan |
| < 55 | Kurang | Belum layak, susun ulang bagian utama |
