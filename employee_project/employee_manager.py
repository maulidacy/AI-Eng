def tampilkan_menu():
    print("=== Manajemen Karyawan Sederhana ===")
    print("1. Tambah Karyawan")
    print("2. Cetak Daftar Karyawan")
    print("3. Cari Karyawan dengan Gaji Tertinggi")
    print("4. Cari Karyawan dengan Gaji Terendah")
    print("5. Hitun Rata-rata Gaji")
    print("6. Keluar")
    print("====================================")

def tambah_karyawan(name, age, salary):
    return {"name": name, "age": age, "salary": salary}

while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:
        print("Masukkan angka antara 1 sampai 6!")
        continue

    if pilihan == 1:
        name = input("Masukkan nama karyawan: ")
        age = int(input("Masukkan umur karyawan: "))
        salary = float(input("Masukkan gaji karyawan: "))
        karyawan = tambah_karyawan(name, age, salary)
        print("Karyawan berhasil ditambahkan!")
    elif pilihan == 2:
        if not karyawan:
            print("Belum ada karyawan yang ditambahkan.")
        else:
            for karyawan in karyawan:
                print(f"Nama: {karyawan['name']}, Umur: {karyawan['age']}, Gaji: {karyawan['salary']}")

