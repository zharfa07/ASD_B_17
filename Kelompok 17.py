import csv
import os

file_name = "data_kelas.csv"

class Node:
  def __init__(self, value):
    self.value = value
    self.kiri = None
    self.kanan = None

class BST:
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
      return
    
    current = self.root
    
    while True:
      if int(value["Nilai"]) < int(current.value["Nilai"]):
        if current.kiri is None:
          current.kiri = Node(value)
          break
        current = current.kiri
      else:
        if current.kanan is None:
          current.kanan = Node(value)
          break
        current = current.kanan
  
  def display(self, node, level=0, prefix="Root: "):
    if node is None:
      return

    print(" " * (level * 4) + prefix + f'({node.value["Nilai"]}) {node.value["Jabatan"]}')

    if node.kiri or node.kanan:
      if node.kiri:
        self.display(node.kiri, level + 1, "L--- ")
      else:
        print(" " * ((level + 1) * 4) + "L--- None")

      if node.kanan:
        self.display(node.kanan, level + 1, "R--- ")
      else:
        print(" " * ((level + 1) * 4) + "R--- None")

def simpan_data(data):
  with open(file_name, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Jabatan", "Nilai"])
    writer.writeheader()
    writer.writerows(data)

def baca_data():
  data = []
  if not os.path.exists(file_name):
    return data
  with open(file_name, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      data.append(row)
  return data

def tambah_data():
  jabatan = input("Masukkan Jabatan: ")
  nilai = input("Masukkan Nilai: ")
  data = baca_data()
  data.append({"Jabatan": jabatan, "Nilai": nilai})
  simpan_data(data)

def tampilkan_bst():
  data = baca_data()
  bst = BST()
  for item in data:
    bst.insert(item)
  if bst.root is None:
    print("Data kosong")
  else:
    bst.display(bst.root)

while True:
  print("\n1. Tambah Data")
  print("2. Tampilkan Struktur Organisasi")
  print("3. Keluar")
  
  pilihan = input("Pilih menu: ")
  
  if pilihan == "1":
    tambah_data()
  elif pilihan == "2":
    tampilkan_bst()
  elif pilihan == "3":
    break
  else:
    print("Input tidak valid")