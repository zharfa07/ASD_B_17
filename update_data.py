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
  elif any(c.isdigit() for c in nama_baru):
    print("Nama tidak valid (mengandung angka)")
    return
  elif any(d["Nama"].lower() == nama_baru.lower() for d in data if d != target):
      print(f"Nama '{nama_baru}' sudah ada")
      return

  for i, j in enumerate(jabatan_valid, 1):
    print(f" {i}. {j}")
  pilihan = input("Jabatan baru (Enter = tidak ubah): ").strip()
  if pilihan == "":
    jabatan_baru = target["Jabatan"]
  elif pilihan.isdigit() and (1 <= int(pilihan) <= len(jabatan_valid)):
      jabatan_baru = jabatan_valid[int(pilihan) - 1]
      if jabatan_baru != "Anggota" and jabatan_baru != target["Jabatan"]:
          if any(d["Jabatan"] == jabatan_baru for d in data if d != target):
              print(f"Jabatan {jabatan_baru} sudah ada")
              return
  else:
      print("Pilihan tidak valid")
      return

  stack.push(f"UBAH | {target['Nama']}/{target['Jabatan']} -> {nama_baru}/{jabatan_baru}")
  target["Nama"] = nama_baru
  target["Jabatan"] = jabatan_baru
  simpan_data(data)
  print("Data berhasil diubah")