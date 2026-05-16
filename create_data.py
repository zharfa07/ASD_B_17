from config import jabatan_valid
from file_handling import baca_data, simpan_data

def create_data(stack):
  print("\n-- Tambah Anggota --")
  nama = input("Nama: ").strip()
  if not nama or any(c.isdigit() for c in nama):
    print("Nama tidak valid")
    return

  for i, j in enumerate(jabatan_valid, 1):
    print(f" {i}. {j}")
  pilihan = input("Nomor jabatan: ").strip()
  if not pilihan.isdigit() or not (1 <= int(pilihan) <= len(jabatan_valid)):
    print("Pilihan tidak valid")
    return

  jabatan = jabatan_valid[int(pilihan) - 1]
  data = baca_data()
  if jabatan != "Anggota" and any(d["Jabatan"] == jabatan for d in data):
    print(f"Jabatan {jabatan} sudah ada")
    return
  if any(d["Nama"].lower() == nama.lower() for d in data):
    print(f"Nama '{nama}' sudah ada")
    return

  data.append({"Nama": nama, "Jabatan": jabatan})
  simpan_data(data)
  stack.push(f"TAMBAH | {nama} | {jabatan}")
  print(f"Berhasil menambahkan {nama} sebagai {jabatan}")
