from config import jabatan_level
from file_handling import baca_data, simpan_data

W = 28
WT = 48

def merge_sort(data, key_func):
  if len(data) <= 1:
    return data
  mid = len(data) // 2
  kiri = merge_sort(data[:mid], key_func)
  kanan = merge_sort(data[mid:], key_func)
  return gabung(kiri, kanan, key_func)

def gabung(kiri, kanan, key_func):
  hasil = []
  i = 0
  j = 0
  while i < len(kiri) and j < len(kanan):
    if key_func(kiri[i]) <= key_func(kanan[j]):
      hasil.append(kiri[i])
      i += 1
    else:
      hasil.append(kanan[j])
      j += 1
  while i < len(kiri):
    hasil.append(kiri[i])
    i += 1
  while j < len(kanan):
    hasil.append(kanan[j])
    j += 1
  return hasil

def sort_data(stack):
  print("\n╔" + "═"*W + "╗")
  print("║" + "URUTKAN DATA".center(W) + "║")
  print("╠" + "═"*W + "╣")
  for b in ["  [1] Nama A-Z","  [2] Nama Z-A","  [3] Hierarki Jabatan"]:
    print("║" + b.ljust(W) + "║")
  print("╚" + "═"*W + "╝")
  pilihan = input("  Pilih: ").strip()
  data = baca_data()
  if not data:
    print("  Data kosong")
    return

  if pilihan == "1":
    hasil = merge_sort(data, lambda x: x["Nama"].lower())
  elif pilihan == "2":
    hasil = merge_sort(data, lambda x: x["Nama"].lower())
    hasil.reverse()
  elif pilihan == "3":
    hasil = merge_sort(data, lambda x: jabatan_level.get(x["Jabatan"], 99))
  else:
    print("  Pilihan tidak valid")
    return

  print("\n╔" + "═"*WT + "╗")
  header = f"  {'No':<5} {'Nama':<25} {'Jabatan'}"
  print("║" + header.ljust(WT) + "║")
  print("╠" + "═"*WT + "╣")
  for i, d in enumerate(hasil, 1):
    baris = f"  {str(i):<5} {d['Nama']:<25} {d['Jabatan']}"
    print("║" + baris.ljust(WT) + "║")
  print("╚" + "═"*WT + "╝")

  if input("\n  Simpan urutan ini ke file? (y/n): ").strip().lower() == "y":
    simpan_data(hasil)
    stack.push(f"SORT | {['A-Z','Z-A','Hierarki'][int(pilihan)-1]}")
    print("  Urutan berhasil disimpan")
