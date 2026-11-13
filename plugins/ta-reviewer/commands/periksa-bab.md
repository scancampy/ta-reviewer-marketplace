---
description: Periksa satu bab tugas akhir terhadap rubriknya (Bab 1-7 atau "pendukung")
argument-hint: "[bab 1-7 | pendukung] (opsional; dosen mengunggah PDF)"
---

Gunakan skill `periksa-bab-ta` untuk memeriksa **satu** bab tugas akhir.

Argumen: `$ARGUMENTS`

Aturan penafsiran argumen:
- Angka 1-7, atau nama bab: pendahuluan (1), landasan teori / tinjauan pustaka (2), analisis (3), perancangan / desain (4), implementasi (5), evaluasi / uji coba / pengujian (6), kesimpulan / saran / kesimpulan dan saran (7).
- `pendukung`, `abstrak`, `daftar pustaka`, atau `lampiran`: mode bagian pendukung (rubrik terpisah).
- Lebih dari satu bab disebutkan: minta dosen memilih satu dahulu.
- Argumen kosong: periksa PDF yang diunggah. Bila PDF berisi beberapa bab, tanya bab mana; bila hanya satu bab, pakai bab yang terdeteksi. Bila belum ada PDF, minta dosen mengunggahnya.

Ikuti alur kerja di SKILL.md `periksa-bab-ta` sampai laporan selesai.
