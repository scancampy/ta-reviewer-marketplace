# ta-reviewer-marketplace

Marketplace berisi plugin **ta-reviewer**: pemeriksa satu bab tugas akhir Teknik Informatika terhadap rubrik per bab.
Umpan balik bersifat pendukung; keputusan nilai tetap di tangan dosen.

## Pasang
```
claude plugin marketplace add NAMA-GITHUB-ANDA/ta-reviewer-marketplace
claude plugin install ta-reviewer@ta-reviewer-marketplace
```
Di dalam sesi Claude Code, gunakan `/plugin marketplace add ...` dan `/plugin install ...`.

## Prasyarat
Skrip pemeriksa membutuhkan Python 3 dan pustaka berikut:
```
pip install -r plugins/ta-reviewer/requirements.txt
```
Render halaman bergambar juga membutuhkan **poppler** (`pdftoppm`) di sistem
(Ubuntu/Debian: `sudo apt install poppler-utils`; macOS: `brew install poppler`).

## Pakai
Unggah PDF tugas akhir (satu bab atau 7 bab sekaligus), lalu jalankan `/periksa-bab 4`
(atau `/periksa-bab perancangan`, `/periksa-bab pendukung`). Detail ada di
[plugins/ta-reviewer/README.md](plugins/ta-reviewer/README.md).

## Catatan
Rubrik bersumber dari slide kuliah Research Methodology. Pastikan Anda berhak membagikannya sebelum repo dibuat publik.
