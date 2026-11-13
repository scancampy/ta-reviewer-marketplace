<!-- Rubrik Bab 4. Salinan bersih dari rubrik asli; isian kosong dan tanda tangan dibuang. Skor dihitung oleh scripts/hitung_skor.py -->

# Rubrik Penilaian Bab 4 (Perancangan / *Design*) Tugas Akhir
**Program Studi Teknik Informatika — Research Methodology**

> Sumber: slide kuliah *Chapter 4 – Design*. Poin bertanda **(slide)** berasal langsung dari slide. Poin bertanda **(pelengkap)** adalah indikator tambahan agar penilaian lebih operasional. Dosen dapat menyesuaikan bobot dan indikator pelengkap sesuai pedoman program studi.

## A. Konteks yang harus diketahui sebelum menilai

- Jenis topik penelitian: ☐ Sistem Informasi ☐ Multimedia ☐ AI/ML ☐ Game ☐ Sistem Pakar ☐ Lainnya: ________

## B. Prinsip Dasar Bab 4 (dari slide)

1. Bab 4 berada **setelah bagian Analisis** (Bab 3) dan **harus merujuk pada analisis sebelumnya**. **(slide)**
2. **Seluruh kebutuhan sistem** dari bagian Analisis harus dipenuhi oleh desain. **(slide)**
3. Tujuan utama bab ini adalah **menjelaskan desain solusi yang diusulkan**, bukan sekadar menampilkan hasil fase desain. **(slide)**
4. Setiap bagian desain harus **dijelaskan**, bukan hanya ditampilkan. **(slide)**
5. Setiap **pertimbangan** dalam proses desain harus dijelaskan secara rinci. **(slide)**
6. **Implementasi** setiap desain dijelaskan di bab Implementasi, bukan di bab ini. **(slide)**
7. **Bagian-bagian bab ini bergantung pada topik penelitian** (lihat tabel di komponen 2). **(slide)**

## C. Ringkasan Bobot

| No | Komponen | Bobot |
|---|---|---|
| 1 | Keterkaitan dengan Analisis dan Kebutuhan Sistem | 20 |
| 2 | Kelengkapan dan Kesesuaian Bagian Desain dengan Topik | 20 |
| 3 | Penjelasan Setiap Bagian dan Pertimbangan Desain | 20 |
| 4 | Landasan Teori dan Analisis (bukan subjektif) | 15 |
| 5 | Ketepatan Notasi dan Efisiensi Representasi | 10 |
| 6 | Batas Desain terhadap Implementasi dan Kesiapan Transisi | 10 |
| 7 | Koherensi, Bahasa, dan Format | 5 |
| | **Total** | **100** |

**Skala level:** 4 = Sangat Baik (100% bobot) · 3 = Baik (75%) · 2 = Cukup (50%) · 1 = Kurang (25%) · 0 = Tidak ada (0%)

**Rumus skor komponen:** `Skor = (Level / 4) × Bobot`

**Komponen yang tidak berlaku (N/A):** Bila suatu bagian desain memang tidak relevan dengan topik (mis. Process Design yang disebut slide sebagai tidak wajib), jangan beri nilai 0. Hitung nilai akhir dengan `skor ÷ bobot yang berlaku × 100`.

## D. Rubrik Rinci per Komponen

### 1. Keterkaitan dengan Analisis dan Kebutuhan Sistem — Bobot 20

**Checklist indikator**
- [ ] Bab 4 merujuk secara eksplisit pada hasil Analisis (Bab 3) **(slide)**
- [ ] **Seluruh** kebutuhan sistem dari Analisis Kebutuhan Sistem terpenuhi oleh desain **(slide)**
- [ ] Keputusan desain tidak bertentangan dengan kebutuhan sistem **(slide: common mistake)**
- [ ] Keterlacakan terlihat jelas, misalnya tabel pemetaan kebutuhan → bagian desain **(pelengkap)**
- [ ] Tidak ada elemen desain yang muncul tanpa dasar kebutuhan **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Setiap kebutuhan sistem tercakup dan dapat ditelusuri ke bagian desain. Tidak ada keputusan desain yang bertentangan atau tanpa dasar. |
| **3** | Hampir semua kebutuhan tercakup. Beberapa keterkaitan hanya tersirat. |
| **2** | Sebagian kebutuhan belum tercakup, atau keterkaitan dengan analisis lemah. |
| **1** | Desain hampir tidak berkaitan dengan kebutuhan sistem, atau bertentangan dengannya. |
| **0** | Tidak ada keterkaitan sama sekali. |

---

### 2. Kelengkapan dan Kesesuaian Bagian Desain dengan Topik — Bobot 20

Bagian bab bervariasi tergantung topik penelitian. **(slide)** Gunakan tabel berikut sebagai acuan bagian yang lazim, bukan daftar baku.

| Topik | Bagian desain yang lazim (slide) |
|---|---|
| Sistem Informasi / terkait | Data design, process design, interface design |
| Multimedia / terkait | Data design, assets design (character, environment, icon, UI/UX), process design, interface design, storyboard design |
| AI / terkait | Dataset design, preprocessing design, feature extraction process design, model classifier design, training process design, model evaluation design, process design dalam aplikasi |
| Game Development / terkait | Data design, gameplay design, assets design (character, environment), process design, interface design |
| Sistem Pakar / terkait | Data design, rule design, process design, interface design |

**Checklist indikator**
- [ ] Bagian desain sesuai jenis topik penelitian **(slide)**
- [ ] Seluruh bagian yang dibutuhkan untuk memenuhi kebutuhan sistem tercakup **(pelengkap)**
- [ ] **Data design:** struktur data yang dipakai dijelaskan, tidak harus basis data (bisa tabel, matriks, variabel, XML, dll.) **(slide)**
- [ ] **Process design:** ada bila dibutuhkan, tetapi **tidak wajib** **(slide)**
- [ ] **Interface/UI/UX design:** hadir bila relevan, ditampilkan dengan Interface Flow Diagram atau representasi setara **(slide)**
- [ ] Bagian khusus topik (mis. desain dataset/model untuk AI, gameplay untuk game, rule untuk sistem pakar) tidak terlewat **(slide)**

| Level | Deskriptor |
|---|---|
| **4** | Seluruh bagian yang relevan dengan topik dan kebutuhan sistem hadir secara lengkap. Tidak ada bagian penting yang terlewat. |
| **3** | Hampir seluruh bagian relevan hadir. Satu bagian kurang lengkap. |
| **2** | Beberapa bagian penting terlewat atau tidak sesuai dengan jenis topik. |
| **1** | Hanya satu atau dua bagian yang hadir, jauh dari yang dibutuhkan topik. |
| **0** | Tidak ada bagian desain. |

---

### 3. Penjelasan Setiap Bagian dan Pertimbangan Desain — Bobot 20

**Checklist indikator**
- [ ] **Setiap bagian desain dijelaskan**, bukan hanya ditampilkan **(slide)**
- [ ] Diagram, flowchart, atau gambar **tidak berdiri sendiri** tanpa atau dengan penjelasan minimum **(slide: common mistake)**
- [ ] **Setiap pertimbangan** dalam proses desain dijelaskan rinci **(slide)**
- [ ] Latar belakang/riset di balik setiap keputusan desain dinyatakan (mengapa dirancang demikian) **(slide: common mistake)**
- [ ] Penjelasan memandu pembaca membaca diagram (alur, elemen penting, istilah) **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Setiap bagian desain disertai penjelasan rinci, termasuk alasan di balik tiap keputusan. Pembaca dapat memahami desain tanpa menebak. |
| **3** | Sebagian besar bagian dijelaskan dengan alasan. Beberapa keputusan hanya dideskripsikan, bukan dijustifikasi. |
| **2** | Penjelasan umumnya hanya menyebut isi diagram, tanpa pertimbangan desain. |
| **1** | Diagram/gambar ditampilkan dengan penjelasan minimum atau tanpa penjelasan. |
| **0** | Tidak ada penjelasan. |

---

### 4. Landasan Teori dan Analisis — Bobot 15

**Checklist indikator**
- [ ] Proses desain **mengacu pada landasan teori** (Bab 2) **(slide: common mistake)**
- [ ] Keputusan desain berdasar teori atau hasil analisis, **bukan** perasaan pribadi, opini pribadi atau teman, atau paparan media/media sosial **(slide)**
- [ ] Prinsip desain yang relevan disebut dan diterapkan (mis. prinsip UI/UX, pola desain, kaidah perancangan model) **(pelengkap)**
- [ ] Sumber acuan keputusan desain dicantumkan (sitasi) **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Seluruh keputusan penting didasarkan pada teori dan/atau hasil analisis dengan rujukan yang jelas. |
| **3** | Sebagian besar keputusan berdasar teori/analisis. Beberapa tanpa rujukan. |
| **2** | Hanya sebagian kecil keputusan berlandaskan teori. Sisanya tanpa dasar. |
| **1** | Desain terutama berdasar opini atau preferensi subjektif. |
| **0** | Tidak ada dasar sama sekali. |

---

### 5. Ketepatan Notasi dan Efisiensi Representasi — Bobot 10

**Checklist indikator**
- [ ] Notasi yang dipakai sesuai dan diterima (ERD, UML, BPMN, DFD, flowchart, Use Case, Interface Flow Diagram, dsb.). Notasi **tidak harus** ERD atau BPMN **(slide)**
- [ ] Untuk notasi yang tidak umum, tersedia **pengantar singkat** mengenai notasi tersebut **(slide)**
- [ ] Notasi digunakan secara konsisten dan benar **(pelengkap)**
- [ ] Bagian yang **memiliki karakteristik khusus** didesain tersendiri **(slide: FAQ)**
- [ ] Bagian yang **serupa** diwakili satu desain dengan keterangan bahwa desain itu berlaku untuk beberapa bagian. Tidak perlu menjelaskan antarmuka yang serupa **(slide)**
- [ ] Jumlah diagram tidak harus sama dengan jumlah proses. Proses yang serupa dapat diwakili satu diagram **(slide: FAQ)**

| Level | Deskriptor |
|---|---|
| **4** | Notasi tepat dan konsisten. Desain serupa dikelompokkan dengan keterangan jelas, dan bagian khusus mendapat desain sendiri. |
| **3** | Notasi tepat. Ada pengulangan yang tidak perlu atau pengelompokan yang kurang jelas. |
| **2** | Notasi kurang konsisten, atau banyak desain serupa diulang tanpa keterangan. |
| **1** | Notasi keliru/tidak dikenal tanpa pengantar, atau bagian khusus tidak didesain. |
| **0** | Tidak ada notasi/representasi. |

---

### 6. Batas Desain terhadap Implementasi dan Kesiapan Transisi — Bobot 10

**Checklist indikator**
- [ ] Bab ini menampilkan **desain**, **bukan hasil implementasi** (mis. tangkapan layar aplikasi jadi, potongan kode final) **(slide: common mistake)**
- [ ] Implementasi tiap desain tidak diuraikan di bab ini melainkan di bab Implementasi **(slide)**
- [ ] Desain dapat diturunkan menjadi bagian bab Implementasi: Database Design → Database Implementation, Process Design → Code Implementation, Interface Design → UI Implementation, Character Design → Character Implementation, Animation Design → Animation Implementation **(slide)**
- [ ] Desain cukup rinci agar dapat dibangun oleh pembaca atau pengembang lain **(pelengkap)**

| Level | Deskriptor |
|---|---|
| **4** | Seluruhnya berupa desain. Setiap bagian dapat diturunkan langsung ke bagian bab Implementasi dan tingkat kerincian memadai. |
| **3** | Sebagian besar berupa desain, dengan sedikit unsur implementasi atau kerincian kurang di beberapa bagian. |
| **2** | Banyak bagian bercampur dengan implementasi, atau desain terlalu umum untuk diwujudkan. |
| **1** | Bab ini terutama menampilkan hasil implementasi. |
| **0** | Tidak ada desain. |

---

### 7. Koherensi, Bahasa, dan Format — Bobot 5

**Checklist indikator** (seluruhnya **pelengkap**)
- [ ] Alur bab runtut (mis. dari data ke proses ke antarmuka, atau sesuai urutan topik)
- [ ] Gambar/tabel bernomor, berjudul, dirujuk dalam teks, dan terbaca jelas
- [ ] Bahasa baku dan sitasi konsisten
- [ ] Istilah konsisten dengan Bab 1–3

| Level | Deskriptor |
|---|---|
| **4** | Alur runtut, gambar terbaca jelas dan dirujuk, bahasa dan format konsisten. |
| **3** | Alur runtut dengan sedikit kesalahan bahasa/format. |
| **2** | Alur kurang runtut atau gambar sulit dibaca. |
| **1** | Alur terputus dan mengganggu pemahaman. |
| **0** | Tidak memenuhi standar. |

## E. Pemeriksaan Kesalahan Umum (*Common Mistakes*)

Dari slide. Centang bila **ditemukan**.

| ☐ | Temuan | Dampak penilaian |
|---|---|---|
| ☐ | Hanya diagram, flowchart, atau gambar tanpa atau dengan penjelasan minimum | Komponen 3 |
| ☐ | Hanya menampilkan desain tanpa penjelasan pertimbangan atau riset di baliknya | Komponen 3 |
| ☐ | Desain tidak merujuk pada kebutuhan sistem, atau bahkan bertentangan dengannya | Komponen 1 |
| ☐ | Proses desain tidak menyebut landasan teori | Komponen 4 |
| ☐ | Desain berdasar hal subjektif (perasaan, opini pribadi/teman, paparan media atau media sosial) | Komponen 4 |
| ☐ | Menampilkan hasil implementasi, bukan desain | Komponen 6 |

## F. Pemeriksaan Konsistensi Silang (cepat)

- [ ] Setiap kebutuhan di Bab 3 memiliki bagian desain yang memenuhinya
- [ ] Teori yang dipakai dalam desain tercantum di Bab 2
- [ ] Setiap bagian desain memiliki padanan di bab **Implementasi**
- [ ] Desain mendukung tujuan penelitian di Bab 1
- [ ] Desain data, proses, dan antarmuka saling konsisten (tidak ada atribut/proses/layar yang hilang antarbagian)

## G. Interpretasi skor

| Rentang | Kategori | Keputusan |
|---|---|---|
| 85–100 | Sangat Baik | Layak, revisi minimal |
| 70–84 | Baik | Layak dengan revisi ringan |
| 55–69 | Cukup | Perlu revisi signifikan |
| < 55 | Kurang | Belum layak, susun ulang bagian utama |
