from config import jabatan_valid
from file_handling import baca_data, simpan_data
from read_data import read_data

W = 28

def update_data(stack):
  print("\n╔" + "═"*W + "╗")
  print("║" + "UBAH DATA".center(W) + "║")
  print("╚" + "═"*W + "╝")
  read_data()
  nama_cari = input("\n  Nama yang ingin diubah: ").strip()
  data = baca_data()

  target = None
  for d in data:
    if d["Nama"].lower() == nama_cari.lower():
      target = d
      break

  if not target:
    print("  Data tidak ditemukan")
    return

  print(f"\n  Data saat ini: {target['Nama']} | {target['Jabatan']}")

  nama_baru = input("  Nama baru (Enter = tidak ubah): ").strip()
  if nama_baru == "":
    nama_baru = target["Nama"]
  else:
    for c in nama_baru:
      if c.isdigit():
        print("  Nama tidak valid (mengandung angka)")
        return
    for d in data:
      if d != target and d["Nama"].lower() == nama_baru.lower():
        print(f"  Nama '{nama_baru}' sudah ada")
        return

  print("\n╔" + "═"*W + "╗")
  for i, j in enumerate(jabatan_valid, 1):
    baris = f"  [{i}] {j}"
    print("║" + baris.ljust(W) + "║")
  print("╚" + "═"*W + "╝")
  pilihan = input("  Jabatan baru (Enter = tidak ubah): ").strip()
  if pilihan == "":
    jabatan_baru = target["Jabatan"]
  elif pilihan.isdigit() and (1 <= int(pilihan) <= len(jabatan_valid)):
    jabatan_baru = jabatan_valid[int(pilihan) - 1]
    if jabatan_baru != "Anggota" and jabatan_baru != target["Jabatan"]:
      for d in data:
        if d != target and d["Jabatan"] == jabatan_baru:
          print(f"  Jabatan {jabatan_baru} sudah ada")
          return
  else:
    print("  Pilihan tidak valid")
    return

  stack.push(f"UBAH | {target['Nama']}/{target['Jabatan']} -> {nama_baru}/{jabatan_baru}")
  target["Nama"] = nama_baru
  target["Jabatan"] = jabatan_baru
  simpan_data(data)
  print("  Data berhasil diubah")
