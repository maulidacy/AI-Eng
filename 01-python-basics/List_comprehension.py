#-------------------------------Data Cleaning Sederhana------------------------------------------
harga = [10000, None, 15000, 20000, None, 18000]

# Gunakan list baru untuk menyimpan data yang sudah dibersihkan
harga_bersih = []

for i in harga:
    if i is not None:
        harga_bersih.append(i) #Kenapa tidak pakai harga.remove(i) dalam loop? Karena remove() mengubah list saat sedang diiterasi, yang bisa menyebabkan elemen terlewat. 

print(harga_bersih)

#versi list comprehension
data_cleaning = [i for i in harga if i is not None] #Bayangkan: "Saya ingin membuat list baru berisi i, dari harga, jika i bukan None."
print(data_cleaning)
exit()

#-------------------------------Menentukan suhu panas dan sejuk----------------------------------
suhu = [30, 28, 33, 35, 31, 29, 36]

label_kategori = ["Panas" if s > 32 else "Sejuk" for s in suhu] #s = suhu (variable)
print(label_kategori)
exit()
#-------------------------------Normalisasi Skor-------------------------------------------------
skor = [60, 70, 90, 100, 85]

skor_normalisasi = [s / 100 for s in skor]

print(skor_normalisasi)
exit()

#-------------------------------Jumlahkan Semua Harga Barang-------------------------------------
daftar_barang = [("apel", 10000), ("jeruk", 15000), ("pisang", 20000), ("mangga", 25000)]
total = 0
for barang in daftar_barang:
    total += barang[1]
print(total)

#versi list comprehension
total = sum([harga for nama, harga in daftar_barang])
print(total)
exit()

#-------------------------------Ambil hanya angka yang lebih dari 50-----------------------------
hasil = [i for i in [12, 45, 23, 67, 90, 34] if i > 50]
print(hasil)
exit()

#-------------------------------Ganjil Genap-------------------------------------
angka = range(1, 21)
hasil = [f"Genap-{i}" if i % 2 == 0 else f"Ganjil-{i}" for i in angka]
print(hasil)
exit()

#-------------------------------Huruf Kapital------------------------------------
nama_buah = ["apel", "pisang", "mangga"]
huruf_kapital = [i.upper() for i in nama_buah]
print(huruf_kapital)
exit()

#-------------------------------Angka Genap--------------------------------------
angka = [1, 2, 3, 4, 5, 6, 7, 8]
genap = [i for i in angka if i % 2 == 0]
print(genap)
exit()

#-------------------------------Kuadrat List-------------------------------------
kuadrat_list = [i**2 for i in range(1, 11)]
print(kuadrat_list)
exit()

#-------------------------------Kombinasi Dua List-------------------------------
buah = ["apel", "pisang", "mangga"]
warna = ["merah", "kuning", "oranye"]

# b ambil dari list buah, w ambil dari list warna
combined = [f"{b} berwarna {w}" for b, w in zip(buah, warna)] #zip menggabungkan dua buah list
print(combined)

#versi loop biasa
combined = []

for b, w in zip(buah, warna):
    combined.append(f"{b} berwarna {w}")

print(combined)
exit()

#-------------------------------Angka Berlabel-------------------------------
angka = list(range(1, 11))
hasil = [f"genap-{i}" if i% 2 == 0 else f"ganjil-{i}" for i in angka]
print(hasil)

#versi loop biasa
angka = list(range(1, 11))
hasil = []

for i in angka:
    if i % 2 == 0:
        hasil.append(f"genap-{i}")
    else:
        hasil.append(f"ganjil-{i}")

print(hasil)
exit()

#-------------------------------Huruf Kapital-------------------------------
buah = ["apel", "jeruk", "nanas", "mangga"]
buah_capital = [f"*{i.upper()}*" for i in buah] # Diapit tanda bintang

# versi tanpa f-string
# buah_capital = ["*" + i.upper() + "*" for i in buah]
print(buah_capital)
exit()

#-------------------------------Filter Nama Pendek-------------------------------
nama = ["Ayu", "Budi", "Putri", "Dian", "Salman", "Rian"]
new_nama = []

for i in nama:
    panjang = len(i)
    if panjang < 5:
        new_nama.append(i)
print(new_nama)

#Versi List Comprehension
new_nama_com = [i for i in nama if len(i) < 5]
print(new_nama_com)
exit()

#-------------------------------Ganda Tiga atau Ganjil-------------------------------
angka = list(range(1, 21))
hasil = []

for i in angka:
    if i % 3 == 0:
        hasil.append("Fizz")
    elif i % 2 != 0:
        hasil.append("Ganjil")
print("\nList biasa: ", hasil)

#Versi List Comprehension
hasil = ["Fizz" if i % 3 == 0 else "Ganjil"
         for i in angka if i % 3 == 0 or i % 2 != 0]
print("\nList Comprehension: ", hasil)

exit()

#------------------------------Kuadrat List-----------------------------
def kuadrat_list(data):
    return [i**2 for i in data]

# Contoh penggunaan:
data = [1, 2, 3, 4, 5]
print(kuadrat_list(data))
#----------------------------------------------------------------------