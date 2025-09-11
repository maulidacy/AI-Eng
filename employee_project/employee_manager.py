karyawan_list = []

while True:
    print("\n==== Manajemen Karyawan Sederhana ====")
    print("1. Tambah Karyawan")
    print("2. Cetak Daftar Karyawan")
    print("3. Cari Karyawan dengan Gaji Tertinggi")
    print("4. Cari Karyawan dengan Gaji Terendah")
    print("5. Hitun Rata-rata Gaji")
    print("6. Keluar")
    print("=======================================")
    
    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:
        print("Masukkan angka antara 1 sampai 6!")
        continue

    if pilihan == 1:
        name = input("Masukkan nama karyawan: ")
        age = int(input("Masukkan umur karyawan: "))
        salary = float(input("Masukkan gaji karyawan: "))
        karyawan_list.append((name, age, salary))
        print("Karyawan berhasil ditambahkan!")
    elif pilihan == 2:
        print("\nDaftar Karyawan:")
        for karyawan in karyawan_list:
            print(f"Nama: {karyawan[0]}, Umur: {karyawan[1]}, Gaji: {karyawan[2]}")
        pass
    elif pilihan == 3:
        print("\nKaryawan dengan gaji tertinggi:")
        if karyawan_list:
         tertinggi = max(karyawan_list, key=lambda karyawan: karyawan[2])
         print(f"Karyawan dengan gaji tertinggi adalah {tertinggi[0]} dengan gaji {tertinggi[2]}")
         pass
    elif pilihan == 5:
        pass
    elif pilihan == 6:
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

