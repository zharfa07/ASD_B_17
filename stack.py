import os

RIWAYAT_FILE = "riwayat.txt"

class Stack:
  def __init__(self):
    self.data = []  # list sbg wadah stack
    # load riwayat dr file kalo ada, biar gk hilang pas program restart
    if os.path.exists(RIWAYAT_FILE):
      with open(RIWAYAT_FILE, "r") as f:
        for line in f.readlines():
          self.data.append(line.strip())  # strip() buang newline di tiap baris

  # tambah item ke atas stack sm langsung simpan ke file
  def push(self, item):
    self.data.append(item)  # append = push ke atas stack
    with open(RIWAYAT_FILE, "a") as f:  # mode "a" = append, gk overwrite
      f.write(item + "\n")

  # kosongin stack sm hapus isi file riwayat
  def clear(self):
    self.data = []
    open(RIWAYAT_FILE, "w").close()  # mode "w" = overwrite dgn kosong
    print("  Riwayat berhasil dihapus")

  # kembaliin list riwayat terbalik
  def tampilkan(self):
    return list(reversed(self.data)) 
