from stack import Stack
from read_data import read_data
from search_data import search_data
from read_tree import read_tree
from sort_data import sort_data
from create_data import create_data
from delete_data import delete_data
from update_data import update_data
from export_pdf import export_pdf
from statistik import statistik

W = 28
stack = Stack()

while True:
  print("\n╔" + "═"*W + "╗")
  print("║" + "STRUKTUR KELAS".center(W) + "║")
  print("╠" + "═"*W + "╣")
  for baris in ["  [1] Tambah Anggota","  [2] Tampilkan Data","  [3] Ubah Data",
                "  [4] Hapus Anggota","  [5] Cari Anggota","  [6] Urutkan Data",
                "  [7] Lihat Pohon Kelas","  [8] Riwayat Aksi","  [9] Statistik",
                " [10] Export PDF","  [0] Keluar"]:
    print("║" + baris.ljust(W) + "║")
  print("╚" + "═"*W + "╝")

  pilihan = input("  Pilih menu: ").strip()

  if pilihan == "1":
    create_data(stack)
  elif pilihan == "2":
    read_data()
  elif pilihan == "3":
    update_data(stack)
  elif pilihan == "4":
    delete_data(stack)
  elif pilihan == "5":
    search_data()
  elif pilihan == "6":
    sort_data(stack)
  elif pilihan == "7":
    read_tree()
  elif pilihan == "8":
    riwayat = stack.tampilkan()
    lebar = max((len(r) + 6 for r in riwayat), default=W)
    lebar = max(lebar, W)
    print("\n╔" + "═"*lebar + "╗")
    print("║" + "RIWAYAT AKSI".center(lebar) + "║")
    print("╠" + "═"*lebar + "╣")
    if not riwayat:
      print("║" + "  Riwayat kosong".ljust(lebar) + "║")
    else:
      for item in riwayat:
        baris = f"  - {item}"
        print("║" + baris.ljust(lebar) + "║")
    print("╚" + "═"*lebar + "╝")
    print("\n╔" + "═"*W + "╗")
    print("║" + "  [1] Hapus semua riwayat".ljust(W) + "║")
    print("║" + "  [2] Kembali".ljust(W) + "║")
    print("╚" + "═"*W + "╝")
    Pilihan = input("  Pilih: ").strip()
    if Pilihan == "1":
      stack.clear()
  elif pilihan == "9":
    statistik()
  elif pilihan == "10":
    export_pdf()
  elif pilihan == "0":
    print("  Program selesai")
    break
  else:
    print("  Input tidak valid")
