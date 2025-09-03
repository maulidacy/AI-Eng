barang = "pensil" 
harga = 2000 
jumlah = 3 
total = harga * jumlah

print(f"Barang: {barang}, Harga: Rp. {harga}, Jumlah: {jumlah}, Total: Rp. {total}")
exit()

#------------------------- 10. Konversi Suhu dari Celcius ke Fahrenheit -------------------------
suhu = int(input("Masukan suhu dalam Celcius: "))
hasil = (suhu * 9/5) + 32 

print(f"{suhu} Celcius = {hasil} Fahrenheit")
exit()

#------------------------- 9. Mengubah Format Desimal -------------------------
nilai = 87.654321
# Mengubah format desimal menjadi 2 angka di belakang koma
nilai = format(nilai, '.2f')
# Mengubah string menjadi float
print(f"Nilai dibulatkan: {nilai}")
exit()

#------------------------- 8. Menggabungkan Teks dan Angka -------------------------
nama = input("Masukan nama Anda: ")
umur = input("Maukkan umur Anda: ")

print(f"Nama kamu adalah {nama} dan usia kamu {umur} tahun.")
exit()

#------------------------- 7. Operasi Aritmatika Dasar -------------------------
a = 5
b = 2

print(f"Hasil penjumlahan {a} + {b} = {a + b}")
print(f"Hasil pembagian {a} / {b} = {a / b}")
exit()

#------------------------- 6.Menyimpan dan Menampilkan Biodata ------------------------- 

nama = "maul"
umur = 20
tinggi = 1.75
mahasiswa = True
print(f"Nama saya {nama}, umur saya {umur} tahun, tinggi saya {tinggi} cm, mahasiswa: {mahasiswa}")
exit()

#------------------------- 5. Hitung Umur Berdasarkan Tahun Lahir -------------------------
# Input tahun lahir dan hitung umur
tahun_lahir = int(input("Masukkan tahun lahir: "))
# Menghitung umur berdasarkan tahun 2025
umur = 2025 - tahun_lahir
# Tampilkan umur
print(f"Umur Anda: {umur} tahun")
#print(f"Umur Anda: {2025 - int(tahun_lahir)} tahun")
exit()

#------------------------- 4. Ubah dan Tampilkan Tipe Data -------------------------
nilaiA = "10"
nilaiB = 5
nilaiC = 2.4

print(f"NilaiA awal: {nilaiA}, Tipe data: {type(nilaiA)}, -> setelah diubah: {int(nilaiA)}, Tipe data: {type(int(nilaiA))}")
print(f"NilaiB awal: {nilaiB}, Tipe data: {type(nilaiB)}, -> setelah diubah: {float(nilaiB)}, Tipe data: {type(str(nilaiB))}")
print(f"NilaiC awal: {nilaiC}, Tipe data: {type(nilaiC)}, -> setelah diubah: {int(nilaiC)}, Tipe data: {type(int(nilaiC))}")
exit()

#------------------------- 3. Hitung dan tampilkan hasil dari: 5 + 2 * 10 - 3 / 2 -------------------------
a = 5
b = 2
c = 10
d = 3
Hitung = a+b*c-d/b
print(f"Hasil perhitungan: {Hitung}")
exit()

#------------------------- 1. Buat 3 variabel: nama (string), umur (integer), tinggi (float) -------------------------
nama = "Budi"
umur = 0
tinggi = 1.75
#------------------------- 2. Cetak kalimat: "Halo, nama saya ___, umur saya ___ tahun." -------------------------
print(f"Nama: {nama}, Umur: {umur} tahun, Tinggi: {tinggi} meter")
exit()









