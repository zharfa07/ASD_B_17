import csv
from config import jabatan_valid
from file_handling import baca_data, simpan_data

W = 28

# buka sm baca file CSV, return None kalo file gk ada
def baca_csv(nama_file):
  try:
    with open(nama_file, newline="") as f:
      reader = csv.DictReader(f)
      hasil = []
      for row in reader:
        hasil.append(dict(row))
      return hasil
  except FileNotFoundError:
    print("  File tidak ditemukan")
    return None

# validasi tiap baris: cek kolom, jabatan valid, duplikat nama, jabatan unik
def validasi(baru, data_lama):
  # kumpulin jabatan unik yg udh kepake
  jabatan_terpakai = []
  for d in data_lama:
    if d["Jabatan"] != "Anggota":
      jabatan_terpakai.append(d["Jabatan"])

  # kumpulin nama yg udh ada
  nama_lama = []
  for d in data_lama:
    nama_lama.append(d["Nama"].lower())

  valid = []
  gagal = 0
  for d in baru:
    # cek kolom wajib ada
    if "Nama" not in d or "Jabatan" not in d:
      gagal += 1
      continue
    # cek jabatan harus valid
    if d["Jabatan"] not in jabatan_valid:
      gagal += 1
      continue
    # skip kalau nama udh ada
    if d["Nama"].lower() in nama_lama:
      gagal += 1
      continue
    # jabatan unik gk boleh dobel
    if d["Jabatan"] != "Anggota" and d["Jabatan"] in jabatan_terpakai:
      gagal += 1
      continue
    valid.append(d)
    # update tracker biar data berikutnya jg dicek
    nama_lama.append(d["Nama"].lower())
    if d["Jabatan"] != "Anggota":
      jabatan_terpakai.append(d["Jabatan"])
  return valid, gagal

def import_data(stack):
  print("\n╔" + "═"*W + "╗")
  print("║" + "IMPORT DATA CSV".center(W) + "║")
  print("╠" + "═"*W + "╣")
  print("║" + "  [1] Tambah ke data lama".ljust(W) + "║")
  print("║" + "  [2] Ganti semua data".ljust(W) + "║")
  print("╚" + "═"*W + "╝")
  pilihan = input("  Pilih: ").strip()
  if pilihan not in ["1", "2"]:
    print("  Pilihan tidak valid")
    return

  nama_file = input("  Nama file CSV: ").strip()
  baru = baca_csv(nama_file)
  if baru is None:
    return
  if not baru:
    print("  File kosong")
    return

  if pilihan == "1":
    # gabung dgn data lama, skip duplikat
    data_lama = baca_data()
    valid, gagal = validasi(baru, data_lama)
    data_lama += valid
    simpan_data(data_lama)
    stack.push(f"IMPORT TAMBAH | {len(valid)} data dari {nama_file}")
    print(f"  Berhasil import {len(valid)} data, {gagal} gagal/duplikat")

  elif pilihan == "2":
    # ganti semua data, minta konfirmasi dulu
    if input("  Yakin ingin mengganti SEMUA data? (y/n): ").strip().lower() != "y":
      print("  Dibatalkan")
      return
    # data_lama kosong karena replace, tp tetap validasi jabatan unik dlm file baru
    valid, gagal = validasi(baru, [])
    simpan_data(valid)
    stack.push(f"IMPORT REPLACE | {len(valid)} data dari {nama_file}")
    print(f"  Berhasil ganti {len(valid)} data, {gagal} gagal")
