# ta-reviewer: pemeriksa bab tugas akhir

Plugin Claude untuk membantu dosen Teknik Informatika memeriksa **satu bab** tugas akhir terhadap rubrik penilaian per bab.
Umpan balik bersifat pendukung; keputusan nilai tetap di tangan dosen.

## Cara pakai
1. Pasang plugin, lalu pasang dependensi: `pip install -r requirements.txt` (dan poppler untuk render halaman).
2. Unggah PDF (satu bab, atau 7 bab dalam satu file) dan jalankan `/periksa-bab 4` (atau `/periksa-bab perancangan`).
3. Jawab pertanyaan singkat: bab mana (bila PDF berisi banyak bab), jenis topik (bab 4-6), dan ringkasan konteks dari bab lain (opsional tetapi meningkatkan akurasi).
4. Terima laporan: skor per komponen, bukti halaman, temuan skrip, butir yang perlu diverifikasi, dan prioritas perbaikan.

`/periksa-bab pendukung` memeriksa Abstrak, Daftar Pustaka, dan Lampiran (rubrik terpisah, butuh PDF lengkap).

## Struktur
```
ta-reviewer/
├── .claude-plugin/plugin.json
├── commands/periksa-bab.md
├── requirements.txt
└── skills/periksa-bab-ta/
    ├── SKILL.md
    ├── scripts/        extract_bab.py · hitung_skor.py · analisis_teks.py
    └── references/     rubrik-bab1..7 · rubrik-pendukung · aturan-umum · panduan-per-bab · konteks-lintas-bab · format-laporan
```

## Mengubah rubrik
Edit file di `references/`. Bobot dibaca dari tabel "Ringkasan Bobot" di tiap rubrik oleh `hitung_skor.py` (total harus 100). Jangan ubah judul tabel itu.

## Batasan
- Hanya satu bab per pemeriksaan; bab lain tidak dibaca (konteks lintas bab lewat ringkasan dosen).
- PDF hasil scan tidak didukung tanpa OCR.
- Hasil skrip (rasio kode, kemiripan, sitasi, tahun sumber, format lampiran) adalah perkiraan dari teks ekstraksi.
- Pemeriksaan visual (diagram, grafik) berbasis sampel halaman (maks. 12 per pemeriksaan).
