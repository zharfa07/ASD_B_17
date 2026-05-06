import csv
import os
from config import file_name

def simpan_data(data):
  with open(file_name, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Nama", "Jabatan"])
    writer.writeheader()
    writer.writerows(data)

def baca_data():
  if not os.path.exists(file_name):
    return []
  with open(file_name, mode="r") as file:
    return list(csv.DictReader(file))
