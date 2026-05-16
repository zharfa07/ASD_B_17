class TreeNode:
  def __init__(self, nama, jabatan):
    self.nama = nama
    self.jabatan = jabatan
    self.children = []

class Tree:
  def __init__(self):
    self.root = None

  def tampilkan(self, node=None, level=0, prefix="Root: "):
    if node is None:
      node = self.root
    if node is None:
      print("Data kosong")
      return
    print(" " * (level * 4) + prefix + f"[{node.jabatan}] {node.nama}")
    for i, child in enumerate(node.children):
      self.tampilkan(child, level + 1, "|--- " if i == 0 else "|--- ")
