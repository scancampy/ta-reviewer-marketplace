#!/usr/bin/env python3
"""Pemeriksaan teks yang bersifat hitungan (deterministik), agar tidak diperkirakan Claude.

Semua hasil adalah PERKIRAAN dari teks hasil ekstraksi PDF. Laporkan ke dosen sebagai perkiraan
yang dapat dikoreksi, bukan sebagai fakta mutlak.

Subperintah:
  tahun-sumber  Persentase sumber <= 5 tahun (Bab 2, komponen 6)
  sitasi        Cocokkan sitasi di naskah dengan daftar pustaka (Bab 2 dan bagian pendukung)
  rasio-kode    Rasio baris penjelasan terhadap baris kode, kode berulang (Bab 5, komponen 4)
  kemiripan     Kalimat yang mirip dengan teks pembanding (Bab 7 komponen 3, abstrak)
  abstrak       Panjang dan jumlah paragraf abstrak
  lampiran      Penomoran lampiran, format halaman, keberadaan user manual
"""
import argparse
import difflib
import json
import re
import sys
from datetime import date

MARKER = re.compile(r"^=== HALAMAN PDF (\d+) ===$")
HURUF = r"A-Za-zÀ-ÿ"


def baca(path):
    return open(path, encoding="utf-8", errors="replace").read()


def per_halaman(teks):
    """[(halaman, [baris...])] dari teks yang memakai penanda '=== HALAMAN PDF n ==='."""
    hasil, cur, h = [], [], None
    for l in teks.splitlines():
        m = MARKER.match(l.strip())
        if m:
            if h is not None:
                hasil.append((h, cur))
            h, cur = int(m.group(1)), []
        else:
            cur.append(l)
    if h is not None:
        hasil.append((h, cur))
    return hasil or [(None, teks.splitlines())]


def tanpa_marker(teks):
    return "\n".join(l for l in teks.splitlines() if not MARKER.match(l.strip()))


# ----------------------------------------------------------------- daftar pustaka & sitasi
def pecah_entri(teks):
    """Pecah daftar pustaka menjadi entri. Entri baru dimulai oleh pola 'Nama, X.' atau '[n]'."""
    baris = [l.strip() for l in tanpa_marker(teks).splitlines() if l.strip()]
    baris = [l for l in baris if not re.fullmatch(r"(DAFTAR PUSTAKA|DAFTAR REFERENSI|REFERENCES|BIBLIOGRAPHY|\d{1,3})", l, re.I)]
    awal = re.compile(rf"^([{HURUF}][{HURUF}'\-]+(?:\s[{HURUF}][{HURUF}'\-]+)?),\s+[A-Z]\.|^\[\d+\]|^[{HURUF}][{HURUF}'\- ]+\.\s*\(")
    entri, cur = [], []
    for l in baris:
        if awal.match(l) and cur:
            entri.append(" ".join(cur))
            cur = [l]
        else:
            cur.append(l)
    if cur:
        entri.append(" ".join(cur))
    return entri


def kunci_entri(e):
    m = re.match(rf"^([{HURUF}][{HURUF}'\-]+)", e)
    y = re.search(r"\(((?:19|20)\d{2})[a-z]?\)", e) or re.search(r"\b((?:19|20)\d{2})\b", e)
    return (m.group(1).lower() if m else None, int(y.group(1)) if y else None)


def ambil_sitasi(teks):
    t = tanpa_marker(teks)
    kunci = set()
    for g in re.findall(r"\(([^()]*?(?:19|20)\d{2}[a-z]?[^()]*?)\)", t):
        for bagian in g.split(";"):
            m = re.search(rf"([{HURUF}][{HURUF}'\-]+)(?:[^;]*?)[,\s]+((?:19|20)\d{{2}})[a-z]?", bagian.strip())
            if m:
                kunci.add((m.group(1).lower(), int(m.group(2))))
    for m in re.finditer(rf"([{HURUF}][{HURUF}'\-]+)(?:\s+(?:et al\.?|dkk\.?|(?:&|dan|and)\s+[{HURUF}][{HURUF}'\-]+))?\s+\(((?:19|20)\d{{2}})[a-z]?\)", t):
        kunci.add((m.group(1).lower(), int(m.group(2))))
    kunci = {k for k in kunci if k[0] not in {"tahun", "gambar", "tabel", "bab", "hal", "halaman", "lihat", "see", "pada", "dalam"}}
    numerik = len(re.findall(r"\[\d+(?:[,\-–]\s*\d+)*\]", t))
    return kunci, numerik


def cocok(k, kunci_pustaka):
    return any(k[1] == y and (k[0] == s or (s and (k[0] in s or s in k[0]))) for s, y in kunci_pustaka)


def cmd_sitasi(a):
    entri = pecah_entri(baca(a.pustaka))
    kp = [kunci_entri(e) for e in entri]
    kunci, numerik = ambil_sitasi(baca(a.naskah))
    tanpa_pustaka = sorted(k for k in kunci if not cocok(k, [x for x in kp if x[0]]))
    dikutip = [e for e, k in zip(entri, kp) if any(k[1] == y and k[0] and (k[0] == s or s in k[0] or k[0] in s) for s, y in kunci)]
    tidak_dikutip = [e[:110] for e, k in zip(entri, kp) if e not in dikutip]
    urutan = []
    nama = [k[0] for k in kp]
    for i in range(1, len(nama)):
        if nama[i] and nama[i - 1] and nama[i] < nama[i - 1]:
            urutan.append(f"'{entri[i][:50]}' muncul setelah '{entri[i-1][:50]}'")
    apa = sum(1 for e in entri if re.search(r"\((?:19|20)\d{2}[a-z]?\)", e))
    hasil = {
        "jumlah_entri_pustaka": len(entri),
        "jumlah_sitasi_unik_di_naskah": len(kunci),
        "entri_berformat_tahun_dalam_kurung": apa,
        "sitasi_bergaya_angka": numerik,
        "sitasi_tanpa_entri_pustaka": [f"{s} ({y})" for s, y in tanpa_pustaka],
        "entri_pustaka_tidak_dikutip": tidak_dikutip,
        "pelanggaran_urutan_alfabet": urutan,
        "jumlah_entri_dikutip": len(dikutip),
        "catatan": "Perkiraan: sitasi dalam gambar/tabel atau penulis bernama majemuk dapat terlewat. Verifikasi sampel manual.",
    }
    if numerik > 5 and apa < len(entri) / 2:
        hasil["catatan_gaya"] = "Sitasi tampak bergaya angka [n], bukan APA."
    if a.simpan_dikutip:
        open(a.simpan_dikutip, "w", encoding="utf-8").write("\n\n".join(dikutip))
        hasil["file_entri_dikutip"] = a.simpan_dikutip
    print(json.dumps(hasil, ensure_ascii=False, indent=2))


def cmd_tahun(a):
    entri = pecah_entri(baca(a.pustaka))
    if a.naskah:
        kunci, _ = ambil_sitasi(baca(a.naskah))
        entri = [e for e in entri if any(kunci_entri(e)[1] == y and kunci_entri(e)[0] and (kunci_entri(e)[0] == s or s in kunci_entri(e)[0]) for s, y in kunci)]
    acuan = a.tahun_acuan or date.today().year
    batas = acuan - 5
    baru, lama, tanpa = 0, [], []
    for e in entri:
        y = kunci_entri(e)[1]
        if y is None:
            tanpa.append(e[:90])
        elif y >= batas:
            baru += 1
        else:
            lama.append(f"{y}: {e[:90]}")
    n = baru + len(lama)
    pct = round(baru / n * 100, 1) if n else None
    if n == 0:
        saran = 0
    elif pct >= 90 and len(lama) <= 2:
        saran = 4
    elif pct >= 70:
        saran = 3
    elif pct >= 40:
        saran = 2
    else:
        saran = 1
    print(json.dumps({
        "tahun_acuan": acuan,
        "ambang": f"tahun >= {batas}",
        "jumlah_sumber_dinilai": len(entri),
        "sumber_5_tahun_terakhir": baru,
        "persen_5_tahun_terakhir": pct,
        "sumber_lama": lama,
        "sumber_tanpa_tahun": tanpa,
        "saran_level_komponen_6": saran,
        "catatan": "Level 4 mensyaratkan sumber lama <= 2 DAN berupa teori klasik yang sah; periksa itu secara manual. Ambang 90/70/40 adalah standar plugin.",
    }, ensure_ascii=False, indent=2))


# ----------------------------------------------------------------- kode (Bab 5)
KATA_KODE = re.compile(
    r"^\s*(def|class|import|from|return|if|else|elif|for|while|function|public|private|protected|static|var|let|const|"
    r"SELECT|INSERT|UPDATE|DELETE|CREATE|FROM|WHERE|JOIN|#include|using|namespace|void|int|float|string|try|catch|except|"
    r"foreach|echo|print|console\.|<\?php|</?[a-z]+[ >])\b", re.I)
KOMENTAR = re.compile(r"^\s*(//|#|/\*|\*|--|<!--|\"\"\")")
KATA_PROSA = re.compile(r"\b(yang|dan|untuk|adalah|dengan|pada|dalam|karena|sehingga|agar|ini|itu|dapat|akan|oleh|dari|serta|the|and|is|of)\b", re.I)


def adalah_prosa(l):
    kata = l.split()
    return len(kata) >= 5 and len(KATA_PROSA.findall(l)) >= 2 and not re.search(r"[;{}]\s*$", l)


def adalah_kode(l):
    s = l.strip()
    if not s or adalah_prosa(s):
        return False
    if re.search(r"[;{}]\s*$", s) or KATA_KODE.match(s) or KOMENTAR.match(s):
        return True
    if re.search(r"(==|!=|=>|->|::|\+=|\)\s*:|\w\(.*\))", s) and len(s.split()) <= 12:
        return True
    if re.match(r"^[\w.\[\]]+\s*=\s*\S", s) and not s.endswith("."):
        return True
    return False


def cmd_kode(a):
    baris = []  # (halaman, teks)
    for h, ls in per_halaman(baca(a.teks)):
        for l in ls:
            if l.strip():
                baris.append((h, l))
    kls = [("K" if adalah_kode(l) else ("P" if adalah_prosa(l.strip()) else "?")) for _, l in baris]
    # blok kode: urutan K, boleh disela maks 1 baris '?'
    blok, i = [], 0
    while i < len(kls):
        if kls[i] != "K":
            i += 1
            continue
        j = i
        while j + 1 < len(kls) and (kls[j + 1] == "K" or (kls[j + 1] == "?" and j + 2 < len(kls) and kls[j + 2] == "K")):
            j += 1
        isi = [baris[k][1] for k in range(i, j + 1)]
        blok.append({"awal": i, "akhir": j, "baris": isi, "halaman": baris[i][0]})
        i = j + 1
    blok = [b for b in blok if len(b["baris"]) >= a.min_baris]

    def prosa_antara(dari, sampai):
        return [k for k in range(dari, sampai) if kls[k] == "P"]

    # gap[i] = baris prosa antara blok i-1 dan blok i (gap[0] = sebelum blok pertama, gap[n] = sesudah blok terakhir)
    gap = []
    for i in range(len(blok) + 1):
        dari = blok[i - 1]["akhir"] + 1 if i > 0 else 0
        sampai = blok[i]["awal"] if i < len(blok) else len(kls)
        g = prosa_antara(dari, sampai)
        gap.append(g[-25:] if i == 0 else (g[:40] if i == len(blok) else g))
    for n, b in enumerate(blok):
        g_sebelum, g_sesudah = gap[n], gap[n + 1]
        # prosa di antara dua blok dibagi dua agar tidak dihitung ganda
        sebelum_n = len(g_sebelum) if n == 0 else len(g_sebelum) - len(g_sebelum) // 2
        sesudah_n = len(g_sesudah) if n == len(blok) - 1 else len(g_sesudah) // 2
        b["baris_kode"] = len(b["baris"])
        b["penjelasan_sebelum"] = sebelum_n
        b["penjelasan_sesudah"] = sesudah_n
        b["penjelasan_total"] = sebelum_n + sesudah_n
        b["rasio"] = round(b["penjelasan_total"] / b["baris_kode"], 2)
        kom = sum(1 for x in b["baris"] if KOMENTAR.match(x))
        b["persen_komentar"] = round(kom / b["baris_kode"] * 100)
        b["tanda_hanya_komentar"] = b["persen_komentar"] >= 30 and b["penjelasan_total"] < 2
        b["cuplikan"] = b["baris"][0].strip()[:70]
    norm = [re.sub(r"\s+", "", "".join(b["baris"])).lower() for b in blok]
    ulang = []
    for x in range(len(blok)):
        for y in range(x + 1, len(blok)):
            if min(len(norm[x]), len(norm[y])) < 40:
                continue
            sm = difflib.SequenceMatcher(None, norm[x], norm[y], autojunk=False)
            if sm.real_quick_ratio() >= a.ambang_mirip and sm.quick_ratio() >= a.ambang_mirip and sm.ratio() >= a.ambang_mirip:
                ulang.append({"blok": [x + 1, y + 1], "halaman": [blok[x]["halaman"], blok[y]["halaman"]], "kemiripan": round(sm.ratio(), 2)})
    ringkas = [{"no": n + 1, "halaman": b["halaman"], "baris_kode": b["baris_kode"], "penjelasan": b["penjelasan_total"],
                "rasio": b["rasio"], "persen_komentar": b["persen_komentar"], "hanya_komentar": b["tanda_hanya_komentar"],
                "awal_kode": b["cuplikan"]} for n, b in enumerate(blok)]
    kurang = [r for r in ringkas if r["rasio"] < 1]
    print(json.dumps({
        "jumlah_listing_terdeteksi": len(blok),
        "listing_penjelasan_lebih_pendek_dari_kode": len(kurang),
        "listing_diduga_hanya_komentar": sum(1 for r in ringkas if r["hanya_komentar"]),
        "pasangan_kode_mirip": ulang,
        "per_listing": ringkas,
        "catatan": "PERKIRAAN heuristik dari teks ekstraksi. Pemisahan kode/penjelasan bisa keliru pada PDF berlayout rumit; "
                   "tinjau halaman yang dirender sebelum menyimpulkan. Kode yang sepele tidak dihitung pada komponen 4 (lihat SKILL.md).",
    }, ensure_ascii=False, indent=2))


# ----------------------------------------------------------------- kemiripan
def kalimat(teks):
    t = re.sub(r"\s+", " ", tanpa_marker(teks))
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý0-9\"'(])", t) if len(s.split()) >= 6]


def token(s):
    return re.findall(r"[a-z0-9À-ÿ]+", s.lower())


def cmd_mirip(a):
    b_tok = token(tanpa_marker(baca(a.pembanding)))
    n = a.n
    ngram_b = {tuple(b_tok[i:i + n]) for i in range(len(b_tok) - n + 1)}
    total, ditandai, daftar = 0, 0, []
    for s in kalimat(baca(a.teks)):
        tk = token(s)
        if len(tk) < n:
            continue
        gs = [tuple(tk[i:i + n]) for i in range(len(tk) - n + 1)]
        frac = sum(1 for g in gs if g in ngram_b) / len(gs)
        total += len(tk)
        if frac >= a.ambang:
            ditandai += len(tk)
            daftar.append({"kemiripan": round(frac, 2), "kalimat": s[:220]})
    daftar.sort(key=lambda d: -d["kemiripan"])
    print(json.dumps({
        "n_gram_kata": n,
        "ambang": a.ambang,
        "persen_kata_dalam_kalimat_mirip": round(ditandai / total * 100, 1) if total else None,
        "jumlah_kalimat_mirip": len(daftar),
        "kalimat_mirip_teratas": daftar[:a.maks],
        "catatan": "Kemiripan tinggi belum tentu salin-tempel (istilah baku/kutipan wajar). Dosen menentukan. "
                   "Teks pembanding hanya diproses skrip ini; Claude tidak membacanya.",
    }, ensure_ascii=False, indent=2))


# ----------------------------------------------------------------- abstrak & lampiran
def cmd_abstrak(a):
    t = baca(a.teks)
    t = tanpa_marker(t)
    blok = [b.strip() for b in re.split(r"\n\s*\n", t) if b.strip()]
    isi = [b for b in blok if not re.match(r"^(ABSTRAK|ABSTRACT)\s*$", b, re.I) and not re.match(r"^(kata kunci|keywords?)\b", b, re.I)]
    baris = [l for l in t.splitlines() if l.strip()]
    kata = len(re.findall(r"\w+", " ".join(isi)))
    print(json.dumps({
        "jumlah_kata_isi": kata,
        "jumlah_baris_teks": len(baris),
        "blok_teks_terpisah_baris_kosong": len(isi),
        "kata_kunci_ada": bool(re.search(r"kata kunci|keywords?", t, re.I)),
        "perkiraan_melebihi_setengah_halaman": kata > a.maks_kata,
        "ambang_kata": a.maks_kata,
        "catatan": "Setengah halaman spasi 1 kira-kira 250-300 kata; ini perkiraan kasar. Jumlah paragraf dari PDF tidak selalu "
                   "terbaca benar: pastikan dari halaman yang dirender.",
    }, ensure_ascii=False, indent=2))


def cmd_lampiran(a):
    judul, hal_fmt, hal_salah, manual = [], [], [], []
    for h, ls in per_halaman(baca(a.teks)):
        ls = [l.strip() for l in ls if l.strip()]
        for l in ls[:4]:
            m = re.match(r"^LAMPIRAN\s+([A-Z])\b[\s.:\-–]*(.*)$", l, re.I)
            if m:
                judul.append({"halaman": h, "huruf": m.group(1), "judul": m.group(2)[:70], "format_judul_benar": m.group(1).isupper()})
        pinggir = ls[:2] + ls[-2:]
        if any(re.fullmatch(r"[A-Z]\s?[-–]\s?\d{1,3}", x) for x in pinggir):
            hal_fmt.append(h)
        elif h is not None:
            hal_salah.append(h)
        if re.search(r"petunjuk penggunaan|buku panduan|manual pengguna|user manual|panduan pengguna|cara penggunaan", " ".join(ls[:6]), re.I):
            manual.append(h)
    print(json.dumps({
        "judul_lampiran_terdeteksi": judul,
        "halaman_berformat_huruf_strip_angka": hal_fmt[:40],
        "halaman_tanpa_format_tersebut": hal_salah[:40],
        "user_manual_ditemukan_di_halaman": manual,
        "catatan": "Format halaman diperiksa dari 2 baris awal/akhir tiap halaman (mis. A-12). Nomor yang disimpan sebagai "
                   "elemen footer terpisah bisa tidak terbaca; verifikasi dari halaman yang dirender.",
    }, ensure_ascii=False, indent=2))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)

    s = sp.add_parser("sitasi")
    s.add_argument("--naskah", required=True)
    s.add_argument("--pustaka", required=True)
    s.add_argument("--simpan-dikutip", help="tulis entri pustaka yang dikutip naskah ke file ini")
    s.set_defaults(f=cmd_sitasi)

    s = sp.add_parser("tahun-sumber")
    s.add_argument("--pustaka", required=True)
    s.add_argument("--naskah", help="bila diberikan, hanya sumber yang dikutip naskah ini yang dihitung")
    s.add_argument("--tahun-acuan", type=int)
    s.set_defaults(f=cmd_tahun)

    s = sp.add_parser("rasio-kode")
    s.add_argument("--teks", required=True)
    s.add_argument("--min-baris", type=int, default=3)
    s.add_argument("--ambang-mirip", type=float, default=0.85)
    s.set_defaults(f=cmd_kode)

    s = sp.add_parser("kemiripan")
    s.add_argument("--teks", required=True)
    s.add_argument("--pembanding", required=True)
    s.add_argument("--n", type=int, default=5)
    s.add_argument("--ambang", type=float, default=0.6)
    s.add_argument("--maks", type=int, default=15)
    s.set_defaults(f=cmd_mirip)

    s = sp.add_parser("abstrak")
    s.add_argument("--teks", required=True)
    s.add_argument("--maks-kata", type=int, default=300)
    s.set_defaults(f=cmd_abstrak)

    s = sp.add_parser("lampiran")
    s.add_argument("--teks", required=True)
    s.set_defaults(f=cmd_lampiran)

    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
