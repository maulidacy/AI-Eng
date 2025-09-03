#---------------------------------Variabel dan Tipe Data---------------------------------
nama = "Budi"
umur = 20
tinggi = 170.5
status_mahasiswa = True
hobi = ["Membaca", "Olahraga", "Bermain Musik"]
data_diri = ("Budi", 20, 170.5)
nilai_ujian = {"Matematika": 90, "Fisika": 85, "Kimia": 88}

print("Nama :", nama, "| Tipe data:", type(nama))
print("Umur :", umur, "| Tipe data:", type(umur))
print("Tinggi :", tinggi, "| Tipe data:", type(tinggi))
print("Status Mahasiswa :", status_mahasiswa, "| Tipe data:", type(status_mahasiswa))
print("Hobi :", hobi, "| Tipe data:", type(hobi))
print("Data diri (nama, umur, tinggi) :", data_diri, "| Tipe data:", type(data_diri))
print("Nilai ujian (Matematika, Fisika, Kimia) :", nilai_ujian,  "| Tipe data:", type(nilai_ujian))
exit()

          
#---------------------------------Program Kalkulator Sederhana---------------------------------
print(40*"=")
print("Program Kalkulator Sederhana")
print(40*"=" + "\n")

operasi_aritmatika = input("Pilih operasi (+, -, *, /): ")
angka_pertama = float(input("Masukkan angka pertama: "))
angka_kedua = float(input("Masukkan angka kedua: "))

if operasi_aritmatika == "+":
    print(f"Hasil: {angka_pertama + angka_kedua}")
elif operasi_aritmatika == "-":
    print(f"Hasil: {angka_pertama - angka_kedua}")
elif operasi_aritmatika == "*":
    print(f"Hasil: {angka_pertama * angka_kedua}")
elif operasi_aritmatika == "/":
    print(f"Hasil: {angka_pertama / angka_kedua}")
else:
    print("Operasi tidak valid. Silakan memilih operasi yang valid.")
exit()


#---------------------------------Menampilkan Bilangan Prima dalam Rentang Tertentu---------------------------------
print(49*"=")
print("Menampilkan Bilangan Prima dalam Rentang Tertentu")
print(49*"=" + "\n")

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

for i in range(bawah, atas + 1):
    if i > 1:  # Bilangan prima harus lebih dari 1
        prima = True  # Anggap bilangan adalah prima
        for j in range(2, int(i**0.5) + 1):  # Cek hingga akar dari i
            if (i % j) == 0:
                prima = False  # Jika ada faktor, bukan prima
                break
        if prima:
            print(f"Bilangan prima: {i}")
exit()
    
#---------------------------------Cek Login dengan Dictionary---------------------------------
print(28*"=")
print("Cek Login dengan Dictionary")
print(28*"=" + "\n")

akun = {"admin": "1234", "user1": "abcd", "user2": "xyz"}

username = input("Masukkan username: ")
password = input("Masukkan password: ")

# Cek apakah username dan password ada di dictionary
if username in akun and akun[username] == password: 
    print("Login Berhasil!")
else:
    print("Login Gagal!")
exit()


#---------------------------------Menghitung Total dalam List---------------------------------
print(28*"=")
print("Menghitung Total dalam List")
print(28*"=" + "\n")

angka = [5, 10, 15, 20, 25]
jumlah = 0

for i in angka:
    jumlah += i
print(f"Total jumlah: {jumlah}")
exit()

#---------------------------------Looping dengan List---------------------------------
print(20*"=")
print("Looping dengan List")
print(20*"=" + "\n")

angka = [10, 20, 30, 40, 50]

for i in angka:
    print(i)
exit()

#---------------------------------Cek Angka Ganjil atau Genap---------------------------------
print(35*"=")
print("Cek Angka Ganjil atau Genap")
print(35*"=" + "\n")

angka = float(input("Masukkan sebuah angka: "))

if angka % 2 == 0:
    print("Angka tersebut adalah genap.")
else:
    print("Angka tersebut adalah ganjil.")
exit()

#---------------------------------Cek Bilangan Positif, Negatif, atau Nol---------------------------------
print(40*"=")
print("Cek Bilangan Positif, Negatif, atau Nol")
print(40*"=" + "\n")

angka = float(input("Masukkan sebuah angka: "))

if angka > 0:
    print("Angka tersebut adalah positif.")
elif angka < 0:
    print("Angka tersebut adalah negatif.")
else:
    print("Angka tersebut adalah nol.")

exit()


#---------------------------------Operasi Aritmatika Sederhana---------------------------------
print(28*"=")
print("Operasi Aritmatika Sederhana")
print(28*"=" + "\n")

angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))
print(f"Penjumlahan: {angka_1 + angka_2}")
print(f"Pengurangan: {angka_1 - angka_2}")
print(f"Perkalian: {angka_1 * angka_2}")
print(f"Pembagian: {angka_1 / angka_2}")

exit()



#---------------------------------Hitung Luas Lingkaran---------------------------------
print(20*"=")
print("Hitung Luas Lingkaran")
print(20*"=" + "\n")

r = float(input("Masukkan jari-jari lingkaran : "))
luas = 3.14 * (r * r)

print(f"Luas lingkaran adalah: {luas}")
exit()



#---------------------------------Deklarasi Variabel---------------------------------
print(20*"=")
print("Deklarasi Variabel")
print(20*"=" + "\n")

angka_bulat = int(input("Angka bulat: "))
print(type(angka_bulat))

angka_pecahan = float(input("Angka pecahan: "))
print(type(angka_pecahan))

teks = input("Teks: ")
print(type(teks))

boolean = bool(input("True/False: "))
print(type(boolean))

input_list = list(input("List: "))
print(type(input_list))

exit()
