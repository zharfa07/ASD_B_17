from config import jabatan_level
from file_handling import baca_data, simpan_data

def sort_data(stack):
  print("\n-- Urutkan Data --")
  print("1. Nama A-Z")
  print("2. Nama Z-A")
  print("3. Hierarki Jabatan")
  pilihan = input("Pilih: ").strip()
  data = baca_data()
  if not data:
    print("Data kosong")
    return

  if pilihan == "1":
    hasil = sorted(data, key=lambda x: x["Nama"].lower())
  elif pilihan == "2":
    hasil = sorted(data, key=lambda x: x["Nama"].lower(), reverse=True)
  elif pilihan == "3":
    hasil = sorted(data, key=lambda x: jabatan_level.get(x["Jabatan"], 99))
  else:
    print("Pilihan tidak valid")
    return

  print(f"{'No':<5} {'Nama':<25} Jabatan")
  print("-" * 45)
  for i, d in enumerate(hasil, 1):
    print(f"{i:<5} {d['Nama']:<25} {d['Jabatan']}")
    
  if input("\nSimpan urutan ini ke file? (y/n): ").strip().lower() == "y":
    simpan_data(hasil)
    stack.push(f"SORT | {['A-Z','Z-A','Hierarki'][int(pilihan)-1]}")
    print("Urutan berhasil disimpan")