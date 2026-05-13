from file_handling import baca_data

def tampilkan_data():
  print("\n-- Daftar Anggota --")
  data = baca_data()
  if not data:
    print("Data kosong")
    return
  print(f"{'No':<5} {'Nama':<25} Jabatan")
  print("-" * 45)
  for i, d in enumerate(data, 1):
    print(f"{i:<5} {d['Nama']:<25} {d['Jabatan']}")
