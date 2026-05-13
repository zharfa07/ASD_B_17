from file_handling import baca_data
from tree import TreeNode, Tree

def read_tree():
  print("\n-- Struktur Kelas --")
  data = baca_data()
  if not data:
    print("Data kosong")
    return

  ketua, level2, anggota = None, [], []
  for item in data:
    node = TreeNode(item["Nama"], item["Jabatan"])
    if item["Jabatan"] == "Ketua Kelas":
      ketua = node
    elif item["Jabatan"] in ["Sekretaris", "Bendahara"]:
      level2.append(node)
    else:
      anggota.append(node)

  if ketua is None:
    print("Ketua Kelas belum ada")
    return

  for node in level2:
    ketua.children.append(node)
  for i, node in enumerate(anggota):
    (level2[i % len(level2)] if level2 else ketua).children.append(node)

  tree = Tree()
  tree.root = ketua
  tree.tampilkan()
