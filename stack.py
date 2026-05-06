class Stack:
  def __init__(self):
    self.data = []

  def push(self, item):
    self.data.append(item)

  def tampilkan(self):
    if not self.data:
      print("Riwayat kosong")
    else:
      for item in reversed(self.data):
        print(" -", item)