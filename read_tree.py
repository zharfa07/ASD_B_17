from file_handling import baca_data
from tree import TreeNode, Tree

def read_tree():
  data = baca_data()
  if not data:
    print("  Data kosong")
    return

  # pisahkan data jd 3 kelompok berdasarkan jabatan
  ketua, level2, anggota = None, [], []
  for item in data:
    node = TreeNode(item["Nama"], item["Jabatan"])
    if item["Jabatan"] == "Ketua Kelas":
      ketua = node  # cmn satu, langsung assign
    elif item["Jabatan"] in ["Sekretaris", "Bendahara"]:
      level2.append(node)  # level 2 di bawah ketua
    else:
      anggota.append(node)  # level paling bawah

  if ketua is None:
    print("  Ketua Kelas belum ada")
    return

  # sekretaris sm bendahara jadi anak dr ketua
  for node in level2:
    ketua.children.append(node)

  # anggota dibagi rata ke level2 secara bergantian pake modulo
  for i, node in enumerate(anggota):
    (level2[i % len(level2)] if level2 else ketua).children.append(node)

  tree = Tree()
  tree.root = ketua  # set ketua sbg root pohon
  tree.tampilkan("POHON KELAS")
