from file_handling import baca_data
from config import jabatan_valid

W = 32

def statistik():
  data = baca_data()
  print("\n╔" + "═"*W + "╗")
  print("║" + "STATISTIK KELAS".center(W) + "║")
  print("╠" + "═"*W + "╣")
  if not data:
    print("║" + "Data kosong".center(W) + "║")
    print("╚" + "═"*W + "╝")
    return
  baris = f"  Total anggota : {len(data)}"
  print("║" + baris + " "*(W - len(baris)) + "║")
  print("╠" + "═"*W + "╣")
  for jabatan in jabatan_valid:
    jumlah = 0
    for d in data:
      if d["Jabatan"] == jabatan:
        jumlah += 1
    baris = f"  {jabatan:<18}: {jumlah}"
    print("║" + baris + " "*(W - len(baris)) + "║")
  print("╚" + "═"*W + "╝")
