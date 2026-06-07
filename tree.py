class TreeNode:
  def __init__(self, nama, jabatan):
    self.nama = nama
    self.jabatan = jabatan
    self.children = []

class Tree:
  def __init__(self):
    self.root = None

  def kumpulkan(self, node=None, level=0, prefix="Root: "):
    if node is None:
      node = self.root
    if node is None:
      return ["Data kosong"]
    baris = " " * (level * 4) + prefix + f"[{node.jabatan}] {node.nama}"
    hasil = [baris]
    for child in node.children:
      hasil += self.kumpulkan(child, level + 1, "└── ")
    return hasil

  def tampilkan(self, judul="POHON KELAS"):
    baris_list = self.kumpulkan()
    lebar = max(max(len(b) for b in baris_list) + 4, len(judul) + 4)
    print("\n╔" + "═"*lebar + "╗")
    print("║" + judul.center(lebar) + "║")
    print("╠" + "═"*lebar + "╣")
    for b in baris_list:
      print("║  " + b.ljust(lebar - 2) + "║")
    print("╚" + "═"*lebar + "╝")
