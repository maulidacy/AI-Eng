angka_rahasia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sudah_benar = False
tebakan = []

for i in angka_rahasia:
    tebakan = int(input("Masukan angka tebakan anda: "))
    if tebakan < 1 or tebakan > 10:
        print("Tebakan terlalu besar!")
    elif tebakan < 1:
        print("Tebakan terlalu kecil!") 
    elif tebakan == angka_rahasia:
        print("Selamat! Tebakan anda benar!")
    sudah_benar = True
    break
exit()
#------------------------Hitung rata-rata nilai dari sekelompok siswa------------------------
daftar_nilai = [85, 90, 78, 92, 88]
total_nilai = 0

for i in daftar_nilai:
    total_nilai += i

# Total nilai siswa bisa didapatkan dengan sum()
# total_nilai = sum(daftar_nilai)

# Jumlah item dalam list bisa didapatkan dengan len()
jumlah_nilai = len(daftar_nilai) 
rata_rata = total_nilai / jumlah_nilai

# Output hasil
print("Total nilai siswa:", total_nilai)
print("Rata-rata nilai siswa:", rata_rata)
exit()

#------------------------Jumlahkan Semua Angka Genap------------------------
angka = [3, 6, 9, 12, 15, 18]
angka_genap = []

for i in angka:
    if i % 2 == 0:
        angka_genap.append(i)

# Gabungkan angka dengan tanda +
hasil_tampilan = " + ".join(str(i) for i in angka_genap) # Menggunakan list comprehension
jumlah_genap = sum(angka_genap)

print(f"{hasil_tampilan} = {jumlah_genap}")
exit()

#------------------------Menghitung Jumlah Bilangan Ganjil dalam List------------------------
angka = [2, 5, 7, 8, 10, 13, 15]
jumlah = 0

for i in angka:
    if i % 2 != 0:
       #print(f"{i} adalah bilangan ganjil")
       jumlah += 1
print(jumlah)
exit()

#------------------------Ganti Semua Elemen Jadi Huruf Kapital------------------------
kata = ["satu", "dua", "tiga"]

#kata_kapital = [kata[0].upper(), kata[1].upper(), kata[2].upper()]
#print(kata_kapital)

#list comprehension
#kata = ["satu", "dua", "tiga"]
#kata_kapital = [i.upper() for i in kata]
#print(kata_kapital)

for i in kata:
    print(i.upper())
exit()

#------------------------Hanya Cetak yang Panjangnya > 5------------------------
buah = ["apel", "pisang", "jeruk", "semangka", "kiwi", "melon", "jambu", "mangga"]

for i in buah:
    panjang = len(i)
    if panjang > 5:
        print(f"{i} ({panjang} huruf)")
exit()

#------------------------Cetak Jumlah Huruf dalam List------------------------
buah = ["apel", "pisang", "jeruk"]

for i in buah:
    print(f"{i} ({len(i)} huruf)")
exit()

#------------------------Cetak list dengan loop------------------------
buah = ["apel", "pisang", "jeruk"]

for i in buah:
    print(i)
exit()

#------------------------Menyusun List dari Input Pengguna------------------------
keranjang = []

while len(keranjang) < 3:
    stok = input(f"Masukkan nama barang ke-{len(keranjang) + 1}: ")
    keranjang.append(stok)

print("\nDaftar barang di keranjang:", keranjang)
exit()

#------------------------Hitung Barang Tertentu-------------------------
pembelian = ["apel", "jeruk", "apel", "anggur", "jeruk", "apel"]
jumlah_apel = pembelian.count("apel") #count() menghitung berapa kali suatu elemen tertentu muncul dalam list
print(f"Jumlah apel yang dibeli: {jumlah_apel}")
exit()

#------------------------ List Bersarang (2 Dimensi)------------------------
barang_dan_harga = [
    ["buku", 15000],
    ["pulpen", 5000],
    ["penghapus", 3000]
]

subtotal = 0

for barang in barang_dan_harga:
    nama = barang[0]
    harga = barang[1]
    print(f"Nama barang: {nama}, Harga barang: Rp. {harga}")
    subtotal += harga

print(f"Subtotal: Rp. {subtotal}")
exit()

#------------------------Menampilkan Jumlah Huruf dalam List (Tanpa Fungsi)------------------------
produk = ["baju", "celana", "jaket", "topi"]

for item in produk:
    print(f"{item} ({len(item)} huruf)")

exit()

#------------------------Ubah Isi List------------------------
barang = ["roti", "susu", "kopi", "teh"]

print("List awal: ", barang)
barang[2] = "kopi hitam"
print("List setelah diganti: ", barang)
exit()

#------------------------Mencari Nilai Tertinggi dalam List------------------------
nilai = [85, 90, 78, 92, 88, 100]

def cek_nilai(nilai):
    return max(nilai)
    #tertinggi = max(nilai)
    #return tertinggi
print(cek_nilai(nilai))
exit()

#------------------------Menghitung Total dan Rata-rata List------------------------
bilangan = [1, 2, 3]

jumlah_nilai = len(bilangan)
total_nilai = sum(bilangan)
rata_rata = total_nilai / jumlah_nilai

print("Bilangan saat ini: ", bilangan)
print("Jumlah bilangan:", jumlah_nilai)
print("Total bilangan:", total_nilai)
print("Rata-rata nilai:", round(rata_rata, 2)) #round() jika ingin rata-rata dibatasi ke 2 desimal
exit()
#------------------------Menampilkan Bilangan Genap dalam List------------------------
bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in bilangan:
    if i % 2 == 0:
        print(f"{i}", end=" ")
exit()

#------------------------Menyusun List dari Input Pengguna------------------------
stok = ["sandal", "sepatu", "tas", "topi"]

print("\nStok saat ini: ", stok)
input_stok = input("Masukkan nama barang: ")
stok.append(input_stok)

print("Update stok: ", stok)
exit()
#------------------------Tambah, Hapus, dan Cetak List------------------------
daftar_belanja = ["apel", "semangka", "anggur"]

daftar_belanja.append("kiwi")
print(daftar_belanja)

if "anggur" in daftar_belanja: #Jika ingin menghindari error saat menghapus item yang tidak ada
    daftar_belanja.remove("anggur")
    print(daftar_belanja)
exit()

#-------------------------------------Filter Nilai dan Kategori----------------------
nilai = [65, 78, 45, 90, 55, 82, 71, 39, 100, 60]

jumlah_siswa_lulus = []
jumlahsiswa_tidak_lulus = []

for i in nilai:
    if i >= 70:
        jumlah_siswa_lulus.append(i)
    else:
        jumlahsiswa_tidak_lulus.append(i)   


print("Jumlah siswa lulus: ", len(jumlah_siswa_lulus))
print("Jumlah siswa tidak lulus: ", len(jumlahsiswa_tidak_lulus))
print("Nilai tertinggi:", max(nilai))
print("Nilai terendah:", min(nilai))
exit()

#----------------------------------------Cek Siswa Lulus-----------------------------
nilai = [55, 90, 77, 65, 80, 40, 95]

# List untuk menyimpan nilai siswa yang lulus
siswa_lulus = []

for n in nilai:
    if n >= 70:
        print("Siswa lulus:", n)
        siswa_lulus.append(n)  # Tambahkan ke list lulus

# Setelah loop selesai, hitung jumlah siswa yang lulus
print("Jumlah siswa yang lulus:", len(siswa_lulus))
print("Daftar nilai siswa lulus:", siswa_lulus)

exit()


#-------------------------------------------------------------------------------
belanja = ["susu", "roti", "keju", "telur", "mentega"]
total_item = 0
belanja.append("kopi") #Tambahkan item "kopi" ke akhir list.
belanja.remove("telur") #Jika ada "telur", hapus dari list.
total_item = len(belanja) #Hitung total item yang tersisa.
print("belanja", belanja, "=", total_item)
exit()

#--------------------------Hapus Buah & Cek Keberadaan--------------------------
buah = ["apel", "pisang", "semangka", "jeruk", "mangga"]

# Hapus "semangka"
buah.remove("semangka") #jika ingin menghapus berdasarkan isi, bukan index.
# Cek apakah "melon" ada di dalam list
print("melon" in buah)
# Cetak list terakhir
print(buah)
exit()
#--------------------------Tambahkan Nilai & Hitung Ulang Rata-rata:--------------------------
nilai = [85, 90, 78, 92, 88]

nilai.append(95)
jumlah_nilai = len(nilai)
total_nilai = sum(nilai)
rata_rata = total_nilai / jumlah_nilai
print("Rata-rata nilai:", rata_rata)
exit()

#-----------------------Rata-rata Nilai dari List-----------------------
nilai = [85, 90, 78, 92, 88]

# Menghitung total, jumlah, dan rata-rata nilai
jumlah_nilai = len(nilai) #menghitung jumlah elemen.
print("Jumlah nilai:", jumlah_nilai)
total_nilai = sum(nilai) #menjumlahkan semua elemen dalam list.
print("Total nilai:", total_nilai)
rata_rata = total_nilai / jumlah_nilai
print("Rata-rata nilai:", rata_rata)
exit()

#------------------------Gabungkan Dua List------------------------
list_1 = ["apel", "jeruk", "mangga"]
list_2 = ["nanas", "semangka"]
list_1.extend(list_2) 
print(list_1)
exit()
#----------------------------Filter Nilai----------------------------
# Program untuk mencetak nilai yang lebih dari 70 dan menghitung jumlahnya
nilai = [55, 80, 72, 90, 65, 40]
jumlah = 0
jumlah_data = 0

for n in nilai:
    if n > 70:
        print(n)        # Cetak nilai yang lebih dari 70
        jumlah_data += 1  # Tambah hitungannya

print("Jumlah nilai di atas 70:", jumlah_data)
exit()

#------------------------Cek Kehadiran Barang------------------------
barang = ["buku", "penghapus", "pensil", "penggaris", "spidol"] 
print("pulpen" in barang) 
barang.append("pulpen")
print(barang)
exit()

#--------------------------Tambah, Hapus, dan Cetak List----------------------------------
belanja = ["roti", "telur", "keju"]
belanja.append("susu") # Menambahkan item baru (susu)
del belanja[1]  # Menghapus item kedua (telur)
print(belanja)
exit()

#------------------------Membalik Kata dalam List------------------------
kata = ["apel", "pisang", "mangga"]
kata_terbalik = kata[::-1]
print(kata_terbalik) 

exit()


#------------------------Mencari Kata Terpanjang dalam List#------------------------
kata = ["aku", "kamu", "dia", "kita", "mereka"]
kata_terpanjang = max(kata, key=len)
print(kata_terpanjang) # Output: mereka
exit()


#------------------------Menyusun List dari Input Pengguna------------------------
name_new = []
i = 0

while True:
    name = input(f"Masukkan nama ke-{i + 1}: ")
    if name == 0:
        break
    name_new.append(name)
    print("List nama: ", name_new)
exit()

#------------------------Menyusun List dari Input Pengguna------------------------
name_new = []
i = 0

while True:
    name = input(f"Masukkan nama ke-{i + 1}: ")
    if name == "0":  # Check for string input "0" to break the loop
        break
    name_new.append(name)
    print("List nama: ", name_new)
    i += 1  # Increment the counter
exit()

#------------------------Menghapus Duplikat dalam List------------------------
angka = [1, 2, 2, 3, 4, 4, 5, 5, 6]

angka_baru = list(set(angka)) # Menghapus duplikat dengan mengubah list menjadi set
print(angka_baru)
exit()


#------------------------Mencari Nilai Maksimum dan Minimum dalam List------------------------
angka = [4, 7, 1, 9, 12, 5]
max_angka = max(angka)
min_angka = min(angka)

print("Nilai maksimum: ", max_angka)
print("Minimum Nilai: ", min_angka)
exit()


#------------------------Menggabungkan dan Mengurutkan Dua List------------------------
list1 = [5, 10, 15]  
list2 = [2, 8, 12]

print("List sebelum digabungkan:")
print("List 1: ", list1)
print("List 2: ", list2)

# Menggabungkan dua list menggunakan fungsi extend() dan sort() untuk mengurutkan list gabungan
list_gabungan = list1.copy()  # Membuat salinan list1
list_gabungan.extend(list2)  # Menggabungkan list2 ke list1

# Mengurutkan list gabungan
list_gabungan.sort()
print("List Gabungan yang Telah Diurutkan: ", list_gabungan)
exit()


#------------------------Menentukan Angka Ganjil dan Genap dalam List------------------------
angka = [10, 15, 20, 25, 30, 35, 40]
ganjil = [x for x in angka if x % 2 != 0]
genap = [x for x in angka if x % 2 == 0]

print("List angka genap: ", genap)
print("List angka ganjil: ", ganjil)
exit()


#------------------------Menghitung Jumlah Kemunculan Elemen dalam List------------------------
angka = [3, 5, 7, 3, 3, 5, 9, 7, 3, 3]
jumlah = angka.count(3)

print(f"Angka 3 muncul sebanyak: {jumlah} kali")
exit()


#------------------------Menyalin dan Membandingkan List------------------------
kota = ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Bali'] 
kota_baru = kota.copy()
kota_baru.append("Yogyakarta")

print("Kota Awal: ", kota)
print("Kota Update: ", kota_baru)

# Membandingkan kedua list
if kota == kota_baru:
    print("List sama.")
else:
    print("List tidak sama.")

exit()



#------------------------Menghitung Total dan Rata-rata List------------------------
angka = [10, 20, 30, 40, 50]
jumlah_angka = len(angka)
total = sum(angka)
rata_rata = total / jumlah_angka

print("Total: ", total)
print("Rata-rata: ", rata_rata)
exit()


#------------------------Menghitung Jumlah Elemen dalam List------------------------
bilangan = [2, 4, 6, 8, 10, 12, 14]
jumlah_bilangan = len(bilangan)

print("Jumlah elemen dalam list: ", jumlah_bilangan)
exit()


#------------------------List 2 Dimensi (Nested List)------------------------
siswa = [
    [10, 12, 14],  # Minggu 1
    [11, 13, 15],  # Minggu 2
    [9, 10, 12]    # Minggu 3
]

print(siswa[1][2]) #Cetak jumlah siswa di minggu ke-2, hari ke-3.
print(siswa[0][0]) #Cetak jumlah siswa di minggu pertama, hari pertama.
exit()



#------------------------Mengurutkan dan Membalik List------------------------
angka = [5, 2, 9, 1, 7]
print("List awal: ", angka)

# Mengurutkan list dalam urutan ascending
angka.sort()
print("List setelah diurutkan: ", angka)
# Membalik list
angka.reverse()
print("List setelah dibalik: ", angka)
exit()


#------------------------Mencari Elemen dalam List------------------------
hewan = ["kucing", "anjing", "kelinci", "sapi"]

for cek in hewan:
    cek = input("cek hewan: ")
    if cek in hewan:
        print(f"{cek} ditemukan")
        break
    else:
        print(f"{cek} tidak ditemukan")
exit()


#------------------------Perulangan dalam List------------------------
name = ["Andi", "Budi", "Cici", "Dodi"]

for i in name:
    print(i)
exit()


#------------------------Menambahkan dan Menghapus Elemen------------------------
angka = []
angka.append(10) #menambahkan
angka.append(20)
angka.append(30)
angka.append(40)
angka.append(50)
angka.remove(30) #menghapus

print(angka)
exit()


#------------------------Mengubah Elemen dalam List------------------------
warna = ["merah", "biru", "hijau", "kuning"]
warna[2] = "ungu"
warna[0] = "hitam"

print(warna)
exit()


#------------------------Buat dan Akses List------------------------
buah = ["apel", "durian", "pisang", "semangka", "jeruk"]
print(buah[0], buah[-3], buah[-1])

print(buah[0])
print(buah[-3])
print(buah[-1])


#--------------------------------
nilai = [70, 80, 90]
total = sum(nilai)
rata2 = total / len(nilai)

print("Total nilai:", total)
print("Banyak data:", len(nilai))
print("Rata-rata nilai adalah:", rata2)
exit()

#------------------------Mengurutkan dan Menghitung Elemen dalam List------------------------
angka = [7, 2, 9, 4, 1]
angka.sort()
print(angka)
print(len(angka))  # untuk melihat jumlah elemen
exit()

#--------------------------------
belanja = []
belanja.extend(["sepatu", "tas", "baju"])
print(belanja)

#pakai append (append hanya bisa satu item)
belanja.append("sepatu")
belanja.append("tas")
belanja.append("baju")

# - - - - - - - - - - - - - - - - - - - 
buah = ["apel", "semangka", "kelengkeng", "anggur", "kiwi"] 
print(buah[2]) 

#-------------------------------------------
buah = ["apel", "jeruk", "mangga", "pisang"]
del buah[1]# Menghapus "jeruk"
buah.pop()# Menghapus item terakhir, yaitu "pisang"
print(buah)# Hasil: ['apel', 'mangga']

#-------------------------------------------
del buah[1]# Menghapus "jeruk"
buah.pop()# Menghapus item terakhir, yaitu "pisang"
print(buah)# Hasil: ['apel', 'mangga']
exit() 

#--------------------Cek Angka 4 muncul berapa kali----------------
angka = [2, 4, 4, 5, 6, 4, 7] 

print(angka.count(4))


exit()
#--------------------Cek Anggota List-----------------
menu = ["nasi goreng", "mie ayam", "soto", "bakso"] 

print("sate" in menu)
print("mie ayam" in menu)
exit() 

#-------------------------------------
nilai = [80, 65, 90, 70, 85]

nilai.sort()# Mengurutkan dari kecil ke besar
print("Nilai yang sudah diurutkan: ", nilai) 

nilai.reverse()# Membalik urutan jadi dari besar ke kecil
nilai.sort()# Mengurutkan dari kecil ke besar
print("Nilai yang sudah diurutkan: ", nilai) 

nilai.reverse()# Membalik urutan jadi dari besar ke kecil
print("Nilai dari terbesar ke terkecil: ", nilai)
exit() 

#-------------------------------------
barang = ["buku", "pulpen", "penggaris", "penghapus", "pensil"] 

print(barang[0], barang[2], barang[4])
exit() 

#-------------------------------------
belanja = []
belanja.extend(["beras", "gula", "minyak"])
print(belanja) 
exit()
