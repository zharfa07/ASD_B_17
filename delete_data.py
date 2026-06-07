from file_handling import baca_data, simpan_data
from read_data import read_data

W = 28

def delete_data(stack):
  print("\n╔" + "═"*W + "╗")
  print("║" + "HAPUS ANGGOTA".center(W) + "║")
  print("╚" + "═"*W + "╝")
  read_data()
  nama_cari = input("\n  Nama yang ingin dihapus: ").strip()
  data = baca_data()

  target = None
  for d in data:
    if d["Nama"].lower() == nama_cari.lower():
      target = d
      break

  if not target:
    print("  Data tidak ditemukan")
    return
  if input(f"  Hapus '{target['Nama']}'? (y/n): ").strip().lower() != "y":
    print("  Dibatalkan")
    return

  data_baru = []
  for d in data:
    if d["Nama"].lower() != nama_cari.lower():
      data_baru.append(d)

  simpan_data(data_baru)
  stack.push(f"HAPUS | {target['Nama']} | {target['Jabatan']}")
  print(f"  {target['Nama']} berhasil dihapus")
