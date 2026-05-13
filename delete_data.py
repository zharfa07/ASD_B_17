from file_handling import baca_data, simpan_data
from read_data import read_data

def delete_data(stack):
  print("\n-- Hapus Anggota --")
  read_data()
  nama_cari = input("\nNama yang ingin dihapus: ").strip()
  data = baca_data()
  target = next((d for d in data if d["Nama"].lower() == nama_cari.lower()), None)
  if not target:
    print("Data tidak ditemukan")
    return
  if input(f"Hapus '{target['Nama']}'? (y/n): ").strip().lower() != "y":
    print("Dibatalkan")
    return
  simpan_data([d for d in data if d["Nama"].lower() != nama_cari.lower()])
  stack.push(f"HAPUS | {target['Nama']} | {target['Jabatan']}")
  print(f"{target['Nama']} berhasil dihapus")
