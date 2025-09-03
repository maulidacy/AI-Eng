#---------------------------------------------nilai lulus------------------------------------------------
nilai = float(input("Masukkan nilai: "))

if nilai >= 60:
    print("Lulus")
else:
    print("Tidak lulus")
exit()

#-------------------------------------Klasifikasi Suhu--------------------------------------
suhu = 25

if suhu < 15:
    print("Dingin")
elif suhu < 25:  # Kondisi ini akan dieksekusi jika suhu antara 15 dan 24
    print("Normal")
else:  # Kondisi ini akan dieksekusi jika suhu 25 atau lebih
    print("Panas")
exit()

#----------------------------------------------------------------------
nilai = float(input("Masukkan nilai ujian: "))

if nilai >= 80:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 60:
    print("C")
else:
    print("D")
exit()
#----------------------------------------------------------------------
angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print(f"Angka {angka} adalah Genap")
elif angka % 2 != 0:
    print(f"Angka {angka} adalah Ganjil")
exit()
#----------------------------------------------------------------------
umur = int(input("Masukkan umur Anda: "))
if umur >= 17:
    print("Selamat. Anda boleh membuat KTP")
elif umur < 17:
    print("Maaf. Belum cukup umur")
exit()

#------------------------- 1. Cek Huruf Vokal -------------------------
huruf = input("Masukan 1 huruf : ") 
huruf_vokal = "a e i o u A E I O U"

if huruf in huruf_vokal:
    print(f"Ya, huruf {huruf} adalah huruf vokal")
else:  
    print(f"Tidak, huruf {huruf} bukan huruf vokal")
exit()

nilai_uts = float(input("Nilai UTS: ")) 
nilai_uas = float(input("Nilai UAS: ")) 
nilai_tugas = float(input("Nilai Tugas: ")) 
Hnilai_uts = nilai_uts * 0.3
Hnilai_uas = nilai_uas * 0.3
Hnilai_tugas = nilai_tugas * 0.4
total_nilai = Hnilai_uts + Hnilai_uas + Hnilai_tugas

if total_nilai >= 85: 
    print("Nilai Akhir = A")
    print("Selamat, Anda lulus dengan nilai A!")
elif total_nilai >= 70: 
    print("Nilai Akhir = B")
    print("Bagus, Anda lulus dengan nilai B!")
elif total_nilai >= 60: 
    print("Nilai Akhir = C")
    print("Anda lulus dengan nilai C, perbaiki di ujian berikutnya.")
else: 
    print("Nilai Akhir = D")
    print("Maaf, Anda tidak lulus. Silakan coba lagi di semester berikutnya.")
exit()

#------------------------- 4. Login Sederhana -------------------------
user = input("username = ") 
passw = input("password = ") 
username = "admin" 
password = "123" 

if user == username and passw == password: 
    print("Login Berhasil!") 
else: 
    print("Login gagal. Coba Lagi!")
exit()

#------------------------- 3. Menghitung Nilai Akhir Mahasiswa ------------------------- 
nilai_uts = float(input("Nilai UTS: ")) 
nilai_uas = float(input("Nilai UAS: ")) 
nilai_tugas = float(input("Nilai Tugas: ")) 
Hnilai_uts = nilai_uts * 0.3
Hnilai_uas = nilai_uas * 0.3
Hnilai_tugas = nilai_tugas * 0.4
total_nilai = Hnilai_uts + Hnilai_uas + Hnilai_tugas

if total_nilai >= 85: 
    print("Nilai Akhir = A")
elif total_nilai >= 70: 
    print("Nilai Akhir = B")
elif total_nilai >= 60: 
    print("Nilai Akhir = C")
else: 
    print("Nilai Akhir = D")
exit()
#------------------------- 2. Cek Bilangan Ganjil atau Genap -------------------------
bilangan = int(input("Masukan bilangan: "))
if bilangan % 2 == 0: 
    print("Bilangan genap")
elif bilangan % 2 != 0:
    print("Bilangan ganjil")
exit()

#------------------------- 1. Cek Angka Positif atau Negatif -------------------------
angka = int(input("Masukkan angka: "))

if angka > 0:
    print("Angka positif")
elif angka < 0:
    print("Angka negatif")
elif angka == 0:
    print("Angka nol")