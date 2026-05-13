# STACK
stack_update = []


def update_data(nama_lama, nama_baru, jabatan_baru):
    data = baca_data()  # fungsi baca data namanya apa

    ditemukan = False

    for row in data:
        if row[0] == nama_lama:

            # Simpan data lama ke stack
            stack_update.append((row[0], row[1]))

            # Update data
            row[0] = nama_baru
            row[1] = jabatan_baru

            ditemukan = True
            break

    if ditemukan:

        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Header
            writer.writerow(["Nama", "Jabatan"])

            # Data baru
            writer.writerows(data)

        print("Data berhasil diupdate.")

    else:
        print("Data tidak ditemukan.")
