from config import jabatan_valid
from file_handling import baca_data

def search_data():
  print("\n-- Cari Anggota --")
  print("1. Cari berdasarkan Nama")
  print("2. Cari berdasarkan Jabatan")
  pilihan = input("Pilih: ").strip()
  data = baca_data()
  if not data:
    print("Data kosong")
    return

  if pilihan == "1":
    keyword = input("Kata kunci: ").strip().lower()
    hasil = [d for d in data if keyword in d["Nama"].lower()]
  elif pilihan == "2":
    for i, j in enumerate(jabatan_valid, 1):
      print(f" {i}. {j}")
    p = input("Nomor jabatan: ").strip()
    if not p.isdigit() or not (1 <= int(p) <= len(jabatan_valid)):
      print("Pilihan tidak valid")
      return
    hasil = [d for d in data if d["Jabatan"] == jabatan_valid[int(p) - 1]]
  else:
    print("Pilihan tidak valid")
    return

  if not hasil:
    print("Data tidak ditemukan")
  else:
    print(f"\n{len(hasil)} data ditemukan:")
    print(f"{'No':<5} {'Nama':<25} Jabatan")
    print("-" * 45)
    for i, d in enumerate(hasil, 1):
      print(f"{i:<5} {d['Nama']:<25} {d['Jabatan']}")
