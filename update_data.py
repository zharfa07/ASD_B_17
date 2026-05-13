from config import jabatan_valid
from file_handling import baca_data, simpan_data
from read_data import read_data

def update_data(stack):
  print("\n-- Ubah Data --")
  read_data()
  nama_cari = input("\nNama yang ingin diubah: ").strip()
  data = baca_data()
  target = next((d for d in data if d["Nama"].lower() == nama_cari.lower()), None)
  if not target:
    print("Data tidak ditemukan")
    return

  print(f"Data saat ini: {target['Nama']} | {target['Jabatan']}")

  nama_baru = input("Nama baru (Enter = tidak ubah): ").strip()
  if nama_baru == "" or any(c.isdigit() for c in nama_baru):
    nama_baru = target["Nama"]

  for i, j in enumerate(jabatan_valid, 1):
    print(f" {i}. {j}")
  pilihan = input("Jabatan baru (Enter = tidak ubah): ").strip()
  if pilihan.isdigit() and (1 <= int(pilihan) <= len(jabatan_valid)):
    jabatan_baru = jabatan_valid[int(pilihan) - 1]
  else:
    jabatan_baru = target["Jabatan"]

  stack.push(f"UBAH | {target['Nama']}/{target['Jabatan']} -> {nama_baru}/{jabatan_baru}")
  target["Nama"] = nama_baru
  target["Jabatan"] = jabatan_baru
  simpan_data(data)
  print("Data berhasil diubah")