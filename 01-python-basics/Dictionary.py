# "key": "value" adalah format dari dictionary
# Dictionary adalah tipe data yang menyimpan data dalam bentuk pasangan key-value.  
# Key bersifat unik, artinya tidak boleh ada key yang sama dalam satu dictionary.
# Nilai dari key bisa berupa tipe data apa saja, termasuk string, integer, list, atau bahkan dictionary itu sendiri.
# Untuk mengakses nilai, kita menggunakan key yang sesuai.

#----------------------------------------------menghitung berapa kali setiap kata muncul di dalam sebuah teks------------------------------------------------
# Input teks
teks = "saya suka makan nasi dan saya suka belajar python"

# kata target yang ingin dihitung kemunculannya
target = ["saya", "python"]

# Dictionary kosong untuk menampung hasil hitung
hitung_kata = {}

# Loop setiap kata dalam teks
for kata in teks.split(): # .split() memecah teks jadi list kata
    if kata in hitung_kata:
        hitung_kata[kata] += 1 # kalau kata sudah ada, jumlahnya ditambah 1
    else:
        hitung_kata[kata] = 1 # kalau kata belum ada, dibuat dengan nilai 1

print("Hasil hitung kata:", hitung_kata)

# Cari kata yang paling sering muncul
kata_terbanyak = max(hitung_kata, key=hitung_kata.get) # max() dengan key=hitungan.get untuk cari kata dengan nilai tertinggi
print(f"Kata yang paling sering muncul: '{kata_terbanyak}' sebanyak {hitung_kata[kata_terbanyak]} kali")

# Cari 3 kata teratas yang paling sering muncul
"""sorted(..., key=lambda item: item[1], reverse=True)
sorted() digunakan untuk mengurutkan.
key=lambda item: item[1] artinya urutkan berdasarkan angka (frekuensi), bukan kata.
item[0] = kata
item[1] = jumlah kemunculan
reverse=True → supaya urut dari besar ke kecil."""

top_3_kata = sorted(hitung_kata.items(), key=lambda item: item[1], reverse=True)[:3] # sorted() dengan key=lambda untuk mengurutkan berdasarkan nilai
print("3 kata teratas yang paling sering muncul:", top_3_kata)

# Hitung total kata unik (kata yang berbeda)
total_kata_unik = len(hitung_kata)
print("Total kata unik:", total_kata_unik)

kata_unik = list(hitung_kata.keys())
print("Kata unik:", kata_unik)
       
# tampilkan hasil hanya sekali
for filter_kataA in set(teks.split()):  # pakai set biar unik
    if filter_kataA in target:
        print("Kata ini masuk:", filter_kataA, hitung_kata[filter_kataA])
exit()

#-------------------------------------------------------------------------------------------------
nilai_siswa = {
    "Maul": 99,
    "Cahya": 88,
    "Kur": 89
}

for nama, nilai in nilai_siswa.items(): # pakai .items(), Python akan memberikan pasangan (key, value) dalam bentuk tuple.
    print(f"Nama: {nama}, Nilai: {nilai}")
exit() 

# -------------------------------------------------------------------------------------------------
hewan = {
    "kucing":"meong",
    "anjing":"guk",
    "ayam":"kukuruyuk"
}

print(hewan["kucing"])
exit()

#-----------------------------------------------------------------------------------------------------------
nilai = {
    "Matematika": 85,
    "Pemrograman": 90,
    "AI": 88
}

# menambah data
nilai["Basis Data"] = 92
print(nilai)

# nilai tertinggi
nilai_tertinggi = max(nilai, key=nilai.get)  # mendapatkan key tertinggi berdasarkan angka

"""key=nilai.get artinya:
Jangan bandingkan key-nya langsung, tapi ambil dulu value dari dictionary."""

print(f"Nilai tertinggi: {nilai_tertinggi} dengan nilai {nilai[nilai_tertinggi]}") # Ambil value dengan indexing [nilai_tertinggi]

#mengakses nilai key
for key in nilai.keys():
    print("key: ", key)

# mengakses nilai value
for value in nilai.values():
    print("value: ", value)
exit()

# ----------------------------------------------------------------------------------------------------------------
mahasiswa = {
    "nama": "Maul",
    "umur": 20,
    "jurusan": "Teknik Informatika"
}

#cetak hanya nama
print(mahasiswa["nama"])

#tambah data baru
mahasiswa["angkatan"] = 2023
print(mahasiswa)

#ubah data
mahasiswa["umur"] = 21

#hapus data
del mahasiswa["jurusan"]
print(mahasiswa)
exit()

#-------------------------------------------------- membuat dict --------------------------------------------------
produk = {
    "nama": "Roti", 
    "harga": 15000, 
    "stok": 20
}

# ambil data
print(produk["nama"])   # Roti

# tambah data
produk["kategori"] = "Makanan"

# ubah data
produk["stok"] = 15

# hapus data
del produk["harga"]

# cek key ada atau tidak
print("stok" in produk)   # True