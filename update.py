import csv
file_name = "data_kelas.csv"

jabatan_valid = [
    "Ketua Kelas",
    "Sekretaris",
    "Bendahara",
    "Anggota"
]

# Stack riwayat update
stack_update = []


def update_data():

    nama_lama = input("Masukkan nama yang ingin diupdate: ")

    data = []

    # Membaca data CSV
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    # Ambil semua nama dari data
    daftar_nama = [row[0] for row in data[1:]]

    # Periksa apakah nama ada
    if nama_lama not in daftar_nama:
        print("Nama tidak ditemukan dalam data.")
        return

    # Jika nama ditemukan
    for row in data[1:]:

        if row[0] == nama_lama:

            # Simpan data lama ke stack
            stack_update.append((row[0], row[1]))

            # Input data baru
            nama_baru = input("Masukkan nama baru: ")
            jabatan_baru = input("Masukkan jabatan baru: ")

            # Validasi jabatan
            while jabatan_baru not in jabatan_valid:
                print("Jabatan tidak valid!")

                jabatan_baru = input("Masukkan jabatan baru: ")

            # Update data
            row[0] = nama_baru
            row[1] = jabatan_baru

            break

    # Simpan perubahan
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerows(data)

    print("\nData berhasil diupdate.")

  

# Jalankan program
update_data()
