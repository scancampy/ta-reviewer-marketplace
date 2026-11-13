#!/usr/bin/env python3
"""Hitung nilai akhir satu bab dari level (0-4 atau N/A) tiap komponen.

Bobot dibaca dari tabel "Ringkasan Bobot" pada file rubrik, jadi perubahan bobot
di rubrik otomatis dipakai. Rumus: skor = (level/4) x bobot.
Nilai akhir = total skor / total bobot yang berlaku x 100.

Contoh:
  python3 hitung_skor.py --bab 2 --level '{"1":3,"2":2,"3":"N/A","4":"N/A","5":3,"6":4,"7":3,"8":3}'
  python3 hitung_skor.py --bab pendukung --level '{"P1":3,"P2":4,"P3":1}'
  python3 hitung_skor.py --bab 5 --level-file level.json --json
"""
import argparse
import json
import os
import re
import sys

REF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references")
BERKAS = {
    "1": "rubrik-bab1-pendahuluan.md",
    "2": "rubrik-bab2-landasan-teori.md",
    "3": "rubrik-bab3-analisis.md",
    "4": "rubrik-bab4-perancangan.md",
    "5": "rubrik-bab5-implementasi.md",
    "6": "rubrik-bab6-evaluasi.md",
    "7": "rubrik-bab7-kesimpulan-dan-saran.md",
    "pendukung": "rubrik-pendukung.md",
}
# Komponen yang lazim boleh N/A menurut rubrik. N/A di luar daftar ini tetap dihitung, tetapi diberi peringatan.
NA_LAZIM = {
    "1": set(),
    "2": {"3", "4"},
    "3": set(),
    "4": set(),
    "5": {"5", "7"},
    "6": set(),
    "7": {"4", "5", "6", "7"},
    "pendukung": set(),
}
KATEGORI = [
    (85, "Sangat Baik", "Layak, revisi minimal"),
    (70, "Baik", "Layak dengan revisi ringan"),
    (55, "Cukup", "Perlu revisi signifikan"),
    (0, "Kurang", "Belum layak, susun ulang bagian utama"),
]
SKALA = {4: "Sangat Baik", 3: "Baik", 2: "Cukup", 1: "Kurang", 0: "Tidak ada"}


def baca_bobot(bab):
    path = os.path.join(REF, BERKAS[bab])
    teks = open(path, encoding="utf-8").read()
    m = re.search(r"Ringkasan Bobot\n(.*?)\n\n", teks, re.S)
    if not m:
        sys.exit(f"Tabel bobot tidak ditemukan di {BERKAS[bab]}")
    komp = {}
    for baris in m.group(1).splitlines():
        sel = [s.strip() for s in baris.strip().strip("|").split("|")]
        if len(sel) >= 3 and re.fullmatch(r"(\d+|P\d+)", sel[0]):
            komp[sel[0]] = (sel[1], int(sel[2]))
    if sum(b for _, b in komp.values()) != 100:
        sys.exit(f"Total bobot di {BERKAS[bab]} bukan 100; periksa rubrik.")
    return komp


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bab", required=True, choices=list(BERKAS))
    ap.add_argument("--level", help='JSON, mis. \'{"1":3,"2":"N/A"}\'')
    ap.add_argument("--level-file")
    ap.add_argument("--json", action="store_true", help="keluarkan JSON, bukan tabel")
    a = ap.parse_args()

    if a.level_file:
        level = json.load(open(a.level_file, encoding="utf-8"))
    elif a.level:
        level = json.loads(a.level)
    else:
        sys.exit("Berikan --level atau --level-file")
    level = {str(k): v for k, v in level.items()}

    komp = baca_bobot(a.bab)
    salah = []
    kurang = [k for k in komp if k not in level]
    ekstra = [k for k in level if k not in komp]
    if kurang:
        salah.append(f"Komponen belum diberi level: {', '.join(kurang)}")
    if ekstra:
        salah.append(f"Komponen tidak dikenal: {', '.join(ekstra)}")

    baris, total, berlaku, peringatan = [], 0.0, 0, []
    for k, (nama, bobot) in komp.items():
        v = level.get(k)
        if v is None:
            continue
        if isinstance(v, str) and v.strip().upper() in ("N/A", "NA"):
            if k not in NA_LAZIM[a.bab]:
                peringatan.append(f"Komponen {k} ({nama}) ditandai N/A padahal tidak lazim; pastikan alasannya dicatat di laporan.")
            baris.append({"no": k, "komponen": nama, "bobot": bobot, "level": "N/A", "skor": None})
            continue
        try:
            lv = int(v)
        except (TypeError, ValueError):
            salah.append(f"Level komponen {k} tidak valid: {v!r}")
            continue
        if lv not in SKALA:
            salah.append(f"Level komponen {k} harus 0-4 atau N/A, bukan {lv}")
            continue
        skor = lv / 4 * bobot
        total += skor
        berlaku += bobot
        baris.append({"no": k, "komponen": nama, "bobot": bobot, "level": lv, "skor": round(skor, 2)})

    if salah:
        sys.exit("KESALAHAN: " + "; ".join(salah))
    if berlaku == 0:
        sys.exit("KESALAHAN: seluruh komponen N/A, nilai tidak dapat dihitung.")
    nilai = total / berlaku * 100
    kat = next((k for batas, k, _ in KATEGORI if nilai >= batas), "")
    keputusan = next((d for batas, _, d in KATEGORI if nilai >= batas), "")
    hasil = {
        "bab": a.bab,
        "komponen": baris,
        "total_skor": round(total, 2),
        "total_bobot_berlaku": berlaku,
        "nilai_akhir": round(nilai, 1),
        "kategori": kat,
        "keputusan_saran": keputusan,
        "peringatan": peringatan,
    }
    if a.json:
        print(json.dumps(hasil, ensure_ascii=False, indent=2))
        return
    print(f"{'No':<4}{'Komponen':<62}{'Bobot':>6}{'Level':>7}{'Skor':>8}")
    for b in baris:
        s = "-" if b["skor"] is None else f"{b['skor']:.2f}"
        print(f"{b['no']:<4}{b['komponen'][:60]:<62}{b['bobot']:>6}{str(b['level']):>7}{s:>8}")
    print(f"\nTotal skor: {hasil['total_skor']}   Total bobot berlaku: {berlaku}")
    print(f"Nilai akhir: {hasil['nilai_akhir']} / 100  ->  {kat} ({keputusan})")
    for p in peringatan:
        print("PERINGATAN:", p)


if __name__ == "__main__":
    main()
