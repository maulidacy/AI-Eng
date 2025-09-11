def tampilkan_menu():
    print("\n=== Manajemen Karyawan Sederhana ===")
    print("1. Tambah Karyawan")
    print("2. Cetak Daftar Karyawan")
    print("3. Cari Karyawan dengan Gaji Tertinggi")
    print("4. Cari Karyawan dengan Gaji Terendah")
    print("5. Hitun Rata-rata Gaji")
    print("6. Keluar")
    print("====================================")

def tambah_karyawan(name, age, salary):
    karyawan.append((name, age, salary))
    return karyawan

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
        karyawan = []
        if not karyawan:
            print("Belum ada karyawan yang ditambahkan.")
        else:
            print("\nDaftar Karyawan:")
            print("-" * 30)
            for name, age, salary in karyawan:
                print(f"Nama: {name}, Umur: {age}, Gaji: {salary}")
            print("-" * 30)
    elif pilihan == 3:
        pass
    elif pilihan == 4:
        pass
    elif pilihan == 5:
        pass
    elif pilihan == 6:
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

