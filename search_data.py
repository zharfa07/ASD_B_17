from config import jabatan_valid
from file_handling import baca_data

W = 28
WT = 48

def search_data():
  print("\n╔" + "═"*W + "╗")
  print("║" + "CARI ANGGOTA".center(W) + "║")
  print("╠" + "═"*W + "╣")
  print("║" + "  [1] Berdasarkan Nama".ljust(W) + "║")
  print("║" + "  [2] Berdasarkan Jabatan".ljust(W) + "║")
  print("╚" + "═"*W + "╝")
  pilihan = input("  Pilih: ").strip()
  data = baca_data()
  if not data:
    print("  Data kosong")
    return

  if pilihan == "1":
    keyword = input("  Masukkan nama: ").strip().lower()
    if not keyword:
      print("  Pilihan tidak valid")
      return
    # cari nama yg mengandung keyword 
    hasil = []
    for d in data:
      if keyword in d["Nama"].lower():
        hasil.append(d)

  elif pilihan == "2":
    print("\n╔" + "═"*W + "╗")
    for i, j in enumerate(jabatan_valid, 1):
      baris = f"  [{i}] {j}"
      print("║" + baris.ljust(W) + "║")
    print("╚" + "═"*W + "╝")
    p = input("  Nomor jabatan: ").strip()
    if not p.isdigit() or not (1 <= int(p) <= len(jabatan_valid)):
      print("  Pilihan tidak valid")
      return
    # filter berdasarkan jabatan yg dipilih
    hasil = []
    for d in data:
      if d["Jabatan"] == jabatan_valid[int(p) - 1]:
        hasil.append(d)
  else:
    print("  Pilihan tidak valid")
    return

  if not hasil:
    print("  Data tidak ditemukan")
  else:
    print(f"\n╔" + "═"*WT + "╗")
    print("║" + f"  {len(hasil)} data ditemukan".ljust(WT) + "║")
    print("╠" + "═"*WT + "╣")
    header = f"  {'No':<5} {'Nama':<25} {'Jabatan'}"
    print("║" + header.ljust(WT) + "║")
    print("╠" + "═"*WT + "╣")
    for i, d in enumerate(hasil, 1):
      baris = f"  {str(i):<5} {d['Nama']:<25} {d['Jabatan']}"
      print("║" + baris.ljust(WT) + "║")
    print("╚" + "═"*WT + "╝")
