import os

RIWAYAT_FILE = "riwayat.txt"

class Stack:
  def __init__(self):
    self.data = []
    if os.path.exists(RIWAYAT_FILE):
      with open(RIWAYAT_FILE, "r") as f:
        for line in f.readlines():
          self.data.append(line.strip())

  def push(self, item):
    self.data.append(item)
    with open(RIWAYAT_FILE, "a") as f:
      f.write(item + "\n")

  def clear(self):
    self.data = []
    open(RIWAYAT_FILE, "w").close()
    print("  Riwayat berhasil dihapus")

  def tampilkan(self):
    return list(reversed(self.data))
