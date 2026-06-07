from config import jabatan_level
from file_handling import baca_data, simpan_data

W = 28
WT = 48

# merge sort: bagi list jadi 2, rekursif sort keduanya, terus gabung
def merge_sort(data, key):
  if len(data) <= 1:
    return data  # base case
  mid = len(data) // 2
  kiri = merge_sort(data[:mid], key)   # rekursif bagian kiri
  kanan = merge_sort(data[mid:], key)  # rekursif bagian kanan
  return gabung(kiri, kanan, key)

# gabungkan dua list yg urut jd satu list urut
def gabung(kiri, kanan, key):
  hasil = []
  i = 0  # pointer list kiri
  j = 0  # pointer list kanan
  # bandingin elemen terdepan kiri dan kanan, masukkin yg lebih kecil
  while i < len(kiri) and j < len(kanan):
    if key(kiri[i]) <= key(kanan[j]):
      hasil.append(kiri[i])
      i += 1
    else:
      hasil.append(kanan[j])
      j += 1
  # kalau masih ada sisa, tambahin ke hasil
  hasil.extend(kiri[i:]) 
  hasil.extend(kanan[j:])

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
    # key = nama lowercase biar A dan a dianggap sama
    hasil = merge_sort(data, lambda x: x["Nama"].lower())
  elif pilihan == "2":
    # sort A-Z dulu lalu balik jadi Z-A
    hasil = merge_sort(data, lambda x: x["Nama"].lower())
    hasil.reverse()
  elif pilihan == "3":
    # key = level hierarki dr config
    hasil = merge_sort(data, lambda x: jabatan_level.get(x["Jabatan"], 99))
  else:
    print("  Pilihan tidak valid")
    return

  # tampilin hasil sort dalam box tabel
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
