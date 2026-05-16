from stack import Stack
from read_data import read_data
from search_data import search_data
from read_tree import read_tree
from sort_data import sort_data
from create_data import create_data
from delete_data import delete_data
from update_data import update_data

stack = Stack()

while True:
  print("\n=== STRUKTUR KELAS ===")
  print("1. Tambah Anggota")
  print("2. Tampilkan Data")
  print("3. Ubah Data")
  print("4. Hapus Anggota")
  print("5. Cari Anggota")
  print("6. Urutkan Data")
  print("7. Lihat Pohon Kelas")
  print("8. Riwayat Aksi")
  print("9. Keluar")

  pilihan = input("Pilih menu: ").strip()

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
    sort_data()
  elif pilihan == "7":
    read_tree()
  elif pilihan == "8":
    print("\n-- Riwayat Aksi --")
    stack.tampilkan()
  elif pilihan == "9":
    print("Program selesai")
    break
  else:
    print("Input tidak valid")