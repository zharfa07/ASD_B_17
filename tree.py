class TreeNode:
  # satu node isi nama, jabatan, dan list anak
  def __init__(self, nama, jabatan):
    self.nama = nama
    self.jabatan = jabatan
    self.children = []  # list node anak 

class Tree:
  def __init__(self):
    self.root = None  # titik awal pohon

  # kumpulin semua baris teks pohon secara rekursif
  def kumpulkan(self, node=None, level=0, prefix="Root: "):
    if node is None:
      node = self.root  # mulai dr root kalo gk ada node yg dikirim
    if node is None:
      return ["Data kosong"]
    # indentasi makin dalem sesuai level, tiap level = 4 spasi
    baris = " " * (level * 4) + prefix + f"[{node.jabatan}] {node.nama}"
    hasil = [baris]
    # rekursif ke tiap anak, level +1 berarti makin dalem
    for child in node.children:
      hasil += self.kumpulkan(child, level + 1, "└── ")
    return hasil  # kembaliin semua baris sbg list

  # tampilkan pohon dlm box, lebar menyesuaikan konten
  def tampilkan(self, judul="POHON KELAS"):
    baris_list = self.kumpulkan()
    # ambil lebar terpanjang antara konten sm judul
    lebar = max(max(len(b) for b in baris_list) + 4, len(judul) + 4)
    print("\n╔" + "═"*lebar + "╗")
    print("║" + judul.center(lebar) + "║")
    print("╠" + "═"*lebar + "╣")
    for b in baris_list:
      print("║  " + b.ljust(lebar - 2) + "║")  # ljust biar border kanan lurus
    print("╚" + "═"*lebar + "╝")
