#!/usr/bin/env python3
"""Deteksi dan ekstrak SATU bab (atau bagian pendukung) dari PDF tugas akhir.

Tujuan: Claude hanya membaca halaman bab yang diperiksa, bukan seluruh buku.

Contoh:
  # 1. Pindai struktur (tidak menulis teks bab, hanya melaporkan batas bab)
  python3 extract_bab.py tugas.pdf --pindai

  # 2. Ekstrak satu bab + pilih halaman bergambar untuk dirender
  python3 extract_bab.py tugas.pdf --bab 4 --out /tmp/periksa --render auto

  # 3. Bagian pendukung (abstrak | daftar-pustaka | lampiran)
  python3 extract_bab.py tugas.pdf --bagian daftar-pustaka --out /tmp/periksa

  # 4. Dump teks seluruh PDF KE FILE untuk diproses skrip saja (Claude tidak membacanya)
  python3 extract_bab.py tugas.pdf --teks-penuh /tmp/periksa/penuh.txt

Keluaran utama berupa JSON di stdout.
"""
import argparse
import json
import os
import re
import sys

from pypdf import PdfReader

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7}
NAMA_BAB = {
    1: "Pendahuluan",
    2: "Landasan Teori",
    3: "Analisis",
    4: "Perancangan",
    5: "Implementasi",
    6: "Evaluasi",
    7: "Kesimpulan dan Saran",
}
KATA_KUNCI = {
    1: ["pendahuluan", "introduction"],
    2: ["landasan teori", "tinjauan pustaka", "kajian pustaka", "dasar teori", "theoretical"],
    3: ["analisis", "analysis"],
    4: ["perancangan", "desain", "rancangan", "design"],
    5: ["implementasi", "implementation"],
    6: ["evaluasi", "uji coba", "pengujian", "evaluation"],
    7: ["kesimpulan", "simpulan", "penutup", "conclusion"],
}
RE_BAB = re.compile(r"^\s*(?:BAB|CHAPTER)\s+([IVX]+|\d+)\b[\s.:\-–—]*(.*)$", re.I)
RE_AKHIR = re.compile(r"^\s*(DAFTAR\s+PUSTAKA|DAFTAR\s+REFERENSI|REFERENCES|BIBLIOGRAPHY|LAMPIRAN)\b", re.I)


def baca_halaman(path):
    r = PdfReader(path)
    teks = []
    for p in r.pages:
        try:
            teks.append(p.extract_text() or "")
        except Exception:
            teks.append("")
    return r, teks


def baris_awal(t, n=8):
    return [l.strip() for l in t.splitlines() if l.strip()][:n]


def nomor_bab(token):
    token = token.upper()
    if token.isdigit():
        return int(token)
    return ROMAN.get(token)


def adalah_toc(t):
    ada = sum(1 for l in t.splitlines() if RE_BAB.match(l))
    titik = len(re.findall(r"\.{4,}", t))
    return ada >= 3 or titik >= 4


def deteksi_bab(teks):
    """Kembalikan list {bab, judul, awal} untuk kemunculan PERTAMA tiap bab (urut naik)."""
    awal = {}
    for i, t in enumerate(teks, start=1):
        if adalah_toc(t):
            continue
        bl = baris_awal(t)
        for j, l in enumerate(bl):
            m = RE_BAB.match(l)
            if not m:
                continue
            n = nomor_bab(m.group(1))
            if not n or not 1 <= n <= 7:
                continue
            judul = m.group(2).strip()
            if not judul and j + 1 < len(bl):
                judul = bl[j + 1]
            if n not in awal:
                awal[n] = {"bab": n, "judul": judul, "awal": i}
            break
    hasil = []
    terakhir = 0
    for n in sorted(awal):
        if awal[n]["awal"] > terakhir:
            hasil.append(awal[n])
            terakhir = awal[n]["awal"]
    return hasil


def akhir_naskah(teks, setelah):
    """Halaman pertama setelah `setelah` yang berjudul Daftar Pustaka / Lampiran."""
    for i in range(setelah, len(teks)):
        if adalah_toc(teks[i]):
            continue
        for l in baris_awal(teks[i], 4):
            if RE_AKHIR.match(l):
                return i  # indeks 0-based => halaman i (1-based) adalah halaman terakhir bab
    return len(teks)


def tentukan_rentang(teks, bab_list):
    rentang = []
    for k, b in enumerate(bab_list):
        if k + 1 < len(bab_list):
            akhir = bab_list[k + 1]["awal"] - 1
        else:
            akhir = akhir_naskah(teks, b["awal"])
        rentang.append({**b, "akhir": max(akhir, b["awal"])})
    return rentang


def tebak_dari_judul(teks):
    for l in baris_awal(teks[0], 6):
        low = l.lower()
        for n, kk in KATA_KUNCI.items():
            if any(k in low for k in kk) and len(l) < 80:
                return n
    return None


def cari_bagian(teks, bagian):
    pola = {
        "abstrak": re.compile(r"^\s*ABSTRAK\b", re.I),
        "daftar-pustaka": re.compile(r"^\s*(DAFTAR\s+PUSTAKA|DAFTAR\s+REFERENSI|REFERENCES|BIBLIOGRAPHY)\b", re.I),
        "lampiran": re.compile(r"^\s*LAMPIRAN\b", re.I),
    }[bagian]
    for i, t in enumerate(teks, start=1):
        if adalah_toc(t) or re.search(r"DAFTAR\s+ISI", "\n".join(baris_awal(t, 3)), re.I):
            continue
        if any(pola.match(l) for l in baris_awal(t, 4)):
            if bagian == "abstrak":
                akhir = i
                for j in range(i, min(i + 2, len(teks))):
                    bl = " ".join(baris_awal(teks[j], 3)).upper()
                    if re.search(r"ABSTRACT|KATA PENGANTAR|DAFTAR ISI|DAFTAR GAMBAR|DAFTAR TABEL|BAB\s", bl):
                        break
                    akhir = j + 1
                return i, akhir
            if bagian == "daftar-pustaka":
                akhir = len(teks)
                for j in range(i, len(teks)):
                    if any(re.match(r"^\s*LAMPIRAN\b", l, re.I) for l in baris_awal(teks[j], 3)):
                        akhir = j
                        break
                return i, max(akhir, i)
            return i, len(teks)
    return None


def tulis_teks(path_out, teks, awal, akhir):
    os.makedirs(os.path.dirname(path_out) or ".", exist_ok=True)
    with open(path_out, "w", encoding="utf-8") as f:
        for i in range(awal, akhir + 1):
            f.write(f"\n=== HALAMAN PDF {i} ===\n{teks[i-1]}\n")


def skor_visual(path, halaman):
    """Hitung jumlah gambar dan elemen vektor per halaman (indikasi diagram/grafik/tabel)."""
    try:
        import pdfplumber
    except ImportError:
        return {}
    hasil = {}
    with pdfplumber.open(path) as pdf:
        for h in halaman:
            try:
                p = pdf.pages[h - 1]
                hasil[h] = {"gambar": len(p.images), "vektor": len(p.rects) + len(p.curves) + len(p.lines)}
            except Exception:
                hasil[h] = {"gambar": 0, "vektor": 0}
    return hasil


def pilih_render(visual, maks):
    def s(v):
        return v["gambar"] * 5 + min(v["vektor"], 200) / 10
    kand = [(h, s(v)) for h, v in visual.items() if s(v) >= 0.5]
    kand.sort(key=lambda x: -x[1])
    pilih = sorted(h for h, _ in kand[:maks])
    return pilih


def render(path, halaman, out_dir, dpi):
    from pdf2image import convert_from_path
    d = os.path.join(out_dir, "render")
    os.makedirs(d, exist_ok=True)
    hasil = []
    for h in halaman:
        try:
            im = convert_from_path(path, dpi=dpi, first_page=h, last_page=h)[0]
            f = os.path.join(d, f"hal_{h:03d}.png")
            im.save(f)
            hasil.append(f)
        except Exception as e:
            print(f"gagal render halaman {h}: {e}", file=sys.stderr)
    return hasil


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--bab", type=int, choices=range(1, 8), help="nomor bab yang diperiksa (1-7)")
    ap.add_argument("--bagian", choices=["abstrak", "daftar-pustaka", "lampiran"])
    ap.add_argument("--pindai", action="store_true", help="hanya laporkan struktur, tanpa menulis teks")
    ap.add_argument("--out", default="/tmp/periksa")
    ap.add_argument("--teks-penuh", help="tulis teks SELURUH PDF ke file ini (untuk skrip, bukan untuk dibaca Claude)")
    ap.add_argument("--render", default="none", help="none | auto | daftar halaman PDF, mis. 12,15,20")
    ap.add_argument("--maks-render", type=int, default=12)
    ap.add_argument("--dpi", type=int, default=70)
    ap.add_argument("--maks-halaman-bab", type=int, default=120, help="peringatan bila bab lebih panjang dari ini")
    a = ap.parse_args()

    reader, teks = baca_halaman(a.pdf)
    total = len(teks)
    rata = sum(len(t) for t in teks) / max(total, 1)
    info = {"file": os.path.basename(a.pdf), "halaman_total": total, "peringatan": []}
    if rata < 100:
        info["peringatan"].append(
            "Teks hampir tidak terbaca (kemungkinan PDF hasil scan). Minta dosen mengunggah PDF yang teksnya "
            "dapat diseleksi, atau jalankan OCR terlebih dahulu. Jangan menilai dari teks kosong."
        )
        info["pdf_scan"] = True

    if a.teks_penuh:
        tulis_teks(a.teks_penuh, teks, 1, total)
        info["teks_penuh"] = a.teks_penuh

    # --- bagian pendukung ---
    if a.bagian:
        r = cari_bagian(teks, a.bagian)
        if not r:
            info["peringatan"].append(f"Bagian '{a.bagian}' tidak ditemukan. Tanyakan halamannya kepada dosen.")
            print(json.dumps(info, ensure_ascii=False, indent=2))
            return
        aw, ak = r
        f = os.path.join(a.out, f"{a.bagian}.txt")
        tulis_teks(f, teks, aw, ak)
        info.update({"bagian": a.bagian, "halaman_awal": aw, "halaman_akhir": ak, "file_teks": f})
        print(json.dumps(info, ensure_ascii=False, indent=2))
        return

    bab_list = tentukan_rentang(teks, deteksi_bab(teks))
    info["bab_terdeteksi"] = [
        {"bab": b["bab"], "judul": b["judul"], "halaman_awal": b["awal"], "halaman_akhir": b["akhir"]} for b in bab_list
    ]
    if len(bab_list) >= 2:
        info["mode"] = "banyak-bab"
    elif len(bab_list) == 1:
        info["mode"] = "satu-bab"
    else:
        tebak = tebak_dari_judul(teks)
        if tebak:
            bab_list = [{"bab": tebak, "judul": NAMA_BAB[tebak], "awal": 1, "akhir": total}]
            info["mode"] = "satu-bab"
            info["bab_terdeteksi"] = [{"bab": tebak, "judul": NAMA_BAB[tebak], "halaman_awal": 1, "halaman_akhir": total, "dugaan": "dari judul halaman pertama"}]
            info["peringatan"].append("Judul 'BAB ...' tidak ditemukan; nomor bab ditebak dari kata kunci judul. Konfirmasi ke dosen.")
        else:
            info["mode"] = "tidak-diketahui"
            info["peringatan"].append("Struktur bab tidak terdeteksi. Tanyakan kepada dosen bab dan halaman yang diperiksa.")

    if a.pindai or info["mode"] == "tidak-diketahui":
        print(json.dumps(info, ensure_ascii=False, indent=2))
        return

    target = a.bab
    if target is None:
        if info["mode"] == "satu-bab":
            target = bab_list[0]["bab"]
        else:
            info["peringatan"].append("File berisi beberapa bab. Tanyakan kepada dosen bab mana yang diperiksa (satu saja).")
            print(json.dumps(info, ensure_ascii=False, indent=2))
            return
    elif info["mode"] == "satu-bab" and bab_list[0]["bab"] != target:
        info["peringatan"].append(
            f"Dosen meminta Bab {target} tetapi file tampak berisi Bab {bab_list[0]['bab']}. Konfirmasi sebelum menilai."
        )
    pilih = next((b for b in bab_list if b["bab"] == target), None)
    if not pilih:
        info["peringatan"].append(f"Bab {target} tidak ditemukan di PDF. Tanyakan halaman awal dan akhirnya kepada dosen.")
        print(json.dumps(info, ensure_ascii=False, indent=2))
        return

    aw, ak = pilih["awal"], pilih["akhir"]
    if ak - aw + 1 > a.maks_halaman_bab:
        info["peringatan"].append(f"Bab ini {ak-aw+1} halaman (> {a.maks_halaman_bab}); periksa apakah batas bab benar.")
    f = os.path.join(a.out, f"bab{target}.txt")
    tulis_teks(f, teks, aw, ak)
    info.update({
        "bab_diperiksa": target,
        "nama_bab": NAMA_BAB[target],
        "halaman_awal": aw,
        "halaman_akhir": ak,
        "file_teks": f,
        "jumlah_karakter": sum(len(teks[i - 1]) for i in range(aw, ak + 1)),
    })

    if a.render != "none":
        rentang = list(range(aw, ak + 1))
        visual = skor_visual(a.pdf, rentang)
        info["halaman_visual"] = [{"halaman": h, **v} for h, v in visual.items() if v["gambar"] or v["vektor"] > 5][:80]
        if a.render == "auto":
            hal = pilih_render(visual, a.maks_render)
        else:
            hal = [int(x) for x in a.render.split(",") if x.strip().isdigit()][: a.maks_render]
        info["halaman_dirender"] = hal
        info["file_gambar"] = render(a.pdf, hal, a.out, a.dpi)
        if len([1 for v in visual.values() if v["gambar"] or v["vektor"] > 5]) > len(hal):
            info["peringatan"].append(
                f"Hanya {len(hal)} halaman bergambar yang dirender (batas {a.maks_render}). Sebutkan di laporan bahwa pemeriksaan visual berbasis sampel."
            )
    print(json.dumps(info, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
