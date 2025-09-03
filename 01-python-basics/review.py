#-----------------------------4. Manajemen List Hewan-----------------------------
nama_hewan = ["Kambing", "Ikan", "Kelinci", "Ayam", "Burung"]

print(f"Daftar hewan awal: {nama_hewan}, jumlah: {len(nama_hewan)}")

# Tambah hewan
tambah_hewan = input("Masukkan nama hewan: ")
nama_hewan.append(tambah_hewan)
print(f"Setelah ditambah: {nama_hewan}, jumlah: {len(nama_hewan)}")

# Hapus hewan (dengan pengecekan)
nama_hapus = input("Masukkan nama hewan yang ingin dihapus: ")
if nama_hapus in nama_hewan:
    nama_hewan.remove(nama_hapus)
    print(f"Setelah dihapus: {nama_hewan}, jumlah: {len(nama_hewan)}")
else:
    print(f"Hewan '{nama_hapus}' tidak ada di daftar!")

# Urutkan
nama_hewan.sort()
print(f"Setelah diurutkan: {nama_hewan}, jumlah: {len(nama_hewan)}")
exit()

#-----------------------------3. Manipulasi list-----------------------------
daftar_makanan = ["nasi goreng", "pizza", "ayam goreng", "soto", "sate"]

# tambah makanan baru
daftar_makanan.append("gudeg")

# hapus makanan jika ada
if "soto" in daftar_makanan:
    daftar_makanan.remove("soto")

# hitung jumlah
jumlah = len(daftar_makanan)

print("Daftar makanan sekarang:", daftar_makanan)
print(f"Jumlah makanan: {jumlah}")
exit()

#-----------------------------2. Rata-rata 3 angka-----------------------------
angka_list = []  # keranjang untuk menyimpan angka

while len(angka_list) < 3:  # selama belum dapat 3 angka
    try:
        angka = float(input(f"Masukkan angka ke-{len(angka_list)+1}: "))
        angka_list.append(angka)  # masukkan ke keranjang
    except ValueError:
        print("Format harus angka!")

# hitung rata-rata
rata_rata = sum(angka_list) / len(angka_list)
print(f"Rata-rata: {rata_rata:.2f}")
exit()
#-----------------------------1. Menghitung Umur-----------------------------
from datetime import datetime # ambil class datetime dari modul datetime

nama = input("Nama: ")

try:
    tahun_lahir = int(input("Tahun lahir: "))
    tahun_sekarang = datetime.now().year # mengambil hanya tahun
    umur = tahun_sekarang - tahun_lahir
    print(f"Halo {nama}, umurmu sekitar {umur} tahun.")
except ValueError:
    print("Tahun lahir harus berupa angka!")

exit()

#-----------------------------------------------------------------------------
# variabel + tipe
nama = "Maulida"
umur = 20
tinggi = 165.5
is_student = True

# output
print("Halo", nama)
print(f"Umur: {umur} tahun, Tinggi: {tinggi} cm")

# operasi aritmatika
x = 10
y = 3
print("Tambah:", x + y)
print("Bagi (float):", x / y)
print("Pembagian bulat:", x // y)
print("Sisa bagi:", x % y)
print("Pangkat:", x ** y)

# list dan dict
buah = ["apel", "pisang", "mangga"]
print("Buah pertama:", buah[0])

mhs = {"nama": "Budi", "nim": "12345"}
print("Nama mahasiswa:", mhs["nama"])

