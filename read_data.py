from file_handling import baca_data

WT = 48

def read_data():
  data = baca_data()
  print("\n╔" + "═"*WT + "╗")
  print("║" + "DAFTAR ANGGOTA".center(WT) + "║")
  print("╠" + "═"*WT + "╣")
  if not data:
    print("║" + "  Data kosong".ljust(WT) + "║")
    print("╚" + "═"*WT + "╝")
    return
  header = f"  {'No':<5} {'Nama':<25} {'Jabatan'}"
  print("║" + header.ljust(WT) + "║")
  print("╠" + "═"*WT + "╣")
  for i, d in enumerate(data, 1):
    baris = f"  {str(i):<5} {d['Nama']:<25} {d['Jabatan']}"
    print("║" + baris.ljust(WT) + "║")
  print("╚" + "═"*WT + "╝")
