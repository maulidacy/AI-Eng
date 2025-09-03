#loop segitiga while
sisi = 6

count = 1
while True:
    print("*" * count)
    count += 1
    
    if count > sisi:
        break
exit()

#loop segitiga for
sisi = 10

count = 1  # dummy variable
for i in range(sisi):
    print("*" * count)
    count += 1  # Increment count
exit()


# Mengulang Input Sampai Benar
print(30*"=")
print("Mengulang Input Sampai Benar")
print(30*"=" + "\n")

password = "python123"
ps = ""

while ps != password:
    ps = input("Masukkan password: ")
    if ps == password:
        print("Password benar! Selamat datang.")
    else:
        print("Password salah! Coba lagi.")
exit()

# Menjumlahkan Bilangan Sampai Nol 
print(35*"=")
print("Menjumlahkan Bilangan Sampai Nol")
print(35*"=" + "\n")

jumlah = 0

while True:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
    if angka == 0:
        break
    jumlah += angka
print("Jumlah total: ", jumlah)
exit()

# Menghitung Angka Genap 
print(25*"=")
print("Menghitung Angka Genap")
print(25*"=" + "\n")

n = int(input("Masukkan angka: "))

# Menghitung jumlah angka genap dari 1 hingga n
jumlah_genap = 0
print("Angka genap:", end=" ")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_genap += 1

print()
print("Jumlah angka genap:", jumlah_genap)
exit()

   

# Menebak Angka
print(14*"=")
print("Menebak Angka")
print(14*"=" + "\n")

angka_rahasia = 7
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    if tebakan == angka_rahasia:
        print("Benar! Anda menang.")
    else:
        print("Salah! Coba lagi.")

exit()


# Hitung Mundur
print(14*"=")
print("Hitung Mundur")
print(14*"=" + "\n")    

n = int(input("Masukkan angka: "))

while 1 <= n:
    print(n)
    n -= 1
    
exit()


# Menampilkan Pola Piramida Angka 
print(32*"=")
print("Menampilkan Pola Piramida Angka")
print(32*"=" + "\n")

tinggi = int(input("Masukkan tinggi piramida: "))
for i in range(1, tinggi + 1): #melakukan iterasi dari 1 hingga tinggi.
    print('*' * i) # mencetak bintang sebanyak i kali, menghasilkan pola segitiga.
exit()

# Hitung Jumlah Huruf dalam Kalimat
print(33*"=")
print("Hitung Jumlah Huruf dalam Kalimat")
print(33*"=" + "\n")

kalimat = input("Masukkan kalimat: ")
huruf = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
jumlah_huruf = 0

for i in huruf:
    jumlah_huruf += kalimat.count(i)
print(f"Jumlah huruf: {jumlah_huruf}")

exit()


# Mengecek Kata Palindrom 
print(23*"=")
print("Mengecek Kata Palindrom")
print(23*"=" + "\n")

kata = input("Masukkan kata: ")

kata_asli = kata # Membuat variabel untuk menyimpan kata yang diinputkan
kata_balik = kata[::-1] # Membuat variabel untuk menyimpan kata yang diinputkan dalam bentuk huruf kebelakang

# Membuat perbandingan antara kata asli dan kata yang diinputkan dalam bentuk huruf ke belakang
if kata == kata_balik:
    print(f"{kata_asli} adalah kata palindrom.")
else:
    print(f"{kata_asli} bukan kata palindrom.")
exit()




# Menghitung Rata-rata Nilai
print(25*"=")
print("Menghitung Rata-rata Nilai")
print(25*"=" + "\n")

n = int(input("Masukkan jumlah mata pelajaran: "))
total_nilai = 0

# Looping untuk meminta input nilai setiap mata pelajaran
for i in range(n):
    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
    total_nilai += nilai
    rata_rata = total_nilai / n
print(f"Rata-rata nilai: {rata_rata}")

exit()


# Kalkulator Diskon
print(20*"=")
print("Kalkulator Diskon")
print(20*"=" + "\n")

harga_barang = float(input("Masukkan harga barang: "))
diskon = float(input("Masukkan persentase diskon: "))

jumlah_diskon = (diskon / 100) * harga_barang
harga_setelah_diskon = harga_barang - jumlah_diskon

print(f"Harga setelah diskon: {harga_setelah_diskon}")
exit()


# Konversi Suhu
print(20*"=")
print("Konversi Suhu")
print(20*"=" + "\n")

suhu = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (suhu * 9/5) + 32
kelvin = suhu + 273.15

print(f"Dalam Fahrenheit: {fahrenheit}")
print(f"Dalam Kelvin: {kelvin}")

exit()