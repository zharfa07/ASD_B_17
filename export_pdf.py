from file_handling import baca_data
from config import jabatan_valid
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_pdf():
  data = baca_data()
  if not data:
    print("Data kosong, tidak bisa export")
    return

  nama_file = "data_kelas.pdf"
  c = canvas.Canvas(nama_file, pagesize=A4)
  lebar, tinggi = A4
  y = tinggi - 50

  c.setFont("Helvetica-Bold", 14)
  c.drawString(50, y, "Data Struktur Kelas")
  y -= 10
  c.line(50, y, lebar - 50, y)
  y -= 25

  c.setFont("Helvetica-Bold", 11)
  c.drawString(50, y, f"{'No':<6}{'Nama':<30}Jabatan")
  y -= 5
  c.line(50, y, lebar - 50, y)
  y -= 18

  c.setFont("Helvetica", 11)
  for i, d in enumerate(data, 1):
    c.drawString(50, y, f"{str(i):<6}{d['Nama']:<30}{d['Jabatan']}")
    y -= 18
    if y < 80:
      c.showPage()
      y = tinggi - 50
      c.setFont("Helvetica", 11)

  y -= 10
  c.line(50, y, lebar - 50, y)
  y -= 20

  c.setFont("Helvetica-Bold", 11)
  c.drawString(50, y, "Statistik:")
  y -= 18

  c.setFont("Helvetica", 11)
  c.drawString(50, y, f"Total anggota: {len(data)}")
  y -= 18

  for jabatan in jabatan_valid:
    jumlah = 0
    for d in data:
      if d["Jabatan"] == jabatan:
        jumlah += 1
    c.drawString(50, y, f"  {jabatan}: {jumlah}")
    y -= 18

  c.save()
  print(f"Berhasil diekspor ke '{nama_file}'")
