karyawan_list = []

while True:
    print("\n==== Manajemen Karyawan Sederhana ====")
    print("1. Tambah Karyawan")
    print("2. Cetak Daftar Karyawan")
    print("3. Cari Karyawan dengan Gaji Tertinggi")
    print("4. Cari Karyawan dengan Gaji Terendah")
    print("5. Rata-rata Gaji")
    print("6. Total Gaji Perusahaan")
    print("7. Hapus Karyawan")
    print("8. Keluar")
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

    elif pilihan == 3:
        print("\nKaryawan dengan gaji tertinggi:")
        if karyawan_list:
         tertinggi = max(karyawan_list, key=lambda karyawan: karyawan[2])
         print(f"{tertinggi[0]} dengan gaji {tertinggi[2]}")
        
    elif pilihan == 4:
        print("\nKaryawan dengan gaji terendah:")
        terendah = min(karyawan_list, key=lambda karyawan: karyawan[2])
        print(f"{terendah[0]} dengan gaji {terendah[2]}")
        
    elif pilihan == 5:
        total_gaji = sum(karyawan[2] for karyawan in karyawan_list)
        jumlah_karyawan = len(karyawan_list)
        rata_rata_gaji = total_gaji / jumlah_karyawan
        print(f"\nRata-rata gaji: {rata_rata_gaji}")

    elif pilihan == 6:
        print("\nTotal gaji perusahaan:")
        total_gaji = sum(karyawan[2] for karyawan in karyawan_list)
        print(f"Total gaji: {total_gaji}")
        
    elif pilihan == 7:
        print("\nHapus Karyawan:")
        name = input("Masukkan nama karyawan yang ingin dihapus: ")
        for karyawan in karyawan_list:
            if karyawan[0] == name:
                karyawan_list.remove(karyawan)
                print("Karyawan berhasil dihapus!")
                break

    elif pilihan == 8:
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

