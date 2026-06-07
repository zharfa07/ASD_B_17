from config import jabatan_valid
from file_handling import baca_data, simpan_data

W = 28

def create_data(stack):
  print("\n╔" + "═"*W + "╗")
  print("║" + "TAMBAH ANGGOTA".center(W) + "║")
  print("╚" + "═"*W + "╝")
  nama = input("  Nama: ").strip()
  if not nama:
    print("  Nama tidak valid")
    return
  for c in nama:
    if c.isdigit():
      print("  Nama tidak valid")
      return

  print("\n╔" + "═"*W + "╗")
  for i, j in enumerate(jabatan_valid, 1):
    baris = f"  [{i}] {j}"
    print("║" + baris.ljust(W) + "║")
  print("╚" + "═"*W + "╝")
  pilihan = input("  Nomor jabatan: ").strip()
  if not pilihan.isdigit() or not (1 <= int(pilihan) <= len(jabatan_valid)):
    print("  Pilihan tidak valid")
    return

  jabatan = jabatan_valid[int(pilihan) - 1]
  data = baca_data()

  if jabatan != "Anggota":
    for d in data:
      if d["Jabatan"] == jabatan:
        print(f"  Jabatan {jabatan} sudah ada")
        return

  for d in data:
    if d["Nama"].lower() == nama.lower():
      print(f"  Nama '{nama}' sudah ada")
      return

  data.append({"Nama": nama, "Jabatan": jabatan})
  simpan_data(data)
  stack.push(f"TAMBAH | {nama} | {jabatan}")
  print(f"  Berhasil menambahkan {nama} sebagai {jabatan}")
