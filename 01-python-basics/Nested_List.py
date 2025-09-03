#-----------------------------------------------------------------------------------------------
# Membuat nested list untuk data siswa
data_siswa = [
    ["Budi", 85, 90],
    ["Siti", 92, 88],
    ["Andi", 78, 85]
]

# Mengakses data
# Mengakses baris pertama (siswa pertama)
siswa_pertama = data_siswa[0]
print(f"Data siswa pertama: {siswa_pertama}")

# Mengakses nama siswa pertama
nama_siswa_pertama = data_siswa[0][0]
print(f"Nama siswa pertama: {nama_siswa_pertama}")

# Mengakses nilai matematika siswa kedua
nilai_matematika_siti = data_siswa[1][1]
print(f"Nilai matematika Siti: {nilai_matematika_siti}")

# Menggunakan perulangan untuk mencetak semua data
print("\n--- Daftar Nilai Siswa ---")
for siswa in data_siswa:
    nama = siswa[0]
    nilai_mat = siswa[1]
    nilai_fis = siswa[2]
    print(f"Nama: {nama}, Nilai Mat: {nilai_mat}, Nilai Fis: {nilai_fis}")
exit()

#--------------------------------------Manajemen Stok Barang----------------------------------------
stok_barang = [
    ["Sepatu", 10, 500000],
    ["Baju", 20, 100000],
    ["Celana", 5, 150000],
    ["Kaos", 15, 75000],
    ["Topi", 8, 50000]
]

print("\n==================================")
print("Daftar barang di gudang saat ini:")
print("==================================")
for barang in stok_barang:
    print(f"{barang[0]} - Jumlah: {barang[1]} - Harga: {barang[2]}")

def tambah_barang(stok_barang):
    try:
        print("\n==================================")
        print("Tambah barang:")
        print("==================================")
        nama_barang = input("Masukkan nama barang: ")
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        harga_barang = int(input("Masukkan harga barang: "))
        stok_barang.append([nama_barang, jumlah_barang, harga_barang])
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka.")
    return stok_barang


def hapus_barang():
    print("\n==================================")
    print("Hapus barang:")
    print("==================================")
    nama_barang = input("Masukkan nama barang: ")
    # Cari index barang
    index_hapus = None
    for i, barang in enumerate(stok_barang):
        if barang[0].lower() == nama_barang.lower():  # bandingkan nama (case-insensitive)
            index_hapus = i
            break

    if index_hapus is not None:
        stok_barang.pop(index_hapus)
    else:
        print("Barang tidak ditemukan di gudang.")
    return index_hapus

#-----------------------------------------------------------------------------------
# lower() di Python dipakai untuk mengubah semua huruf di string menjadi huruf kecil
# Kenapa .pop() bukan .remove()?
# .remove() → harus kasih elemen list yang sama persis.
# .pop(index) → menghapus berdasarkan posisi/index di list.
#-----------------------------------------------------------------------------------

#urutkan
def urutkan_barang():
    stok_barang.sort(key=lambda x: x[0])
    return stok_barang

def tampilkan_barang():
    print("\n==================================")
    print("Daftar barang di gudang saat ini:")
    print("==================================")
    for barang in stok_barang:
        print(f"{barang[0]} - Jumlah: {barang[1]} - Harga: {barang[2]}")
    return stok_barang

#hitung jumlah item tertentu
cari = input("Masukkan nama barang yang ingin dicek jumlahnya: ")
for barang in stok_barang:
    if barang[0].lower() == cari.lower():  # cocokkan nama tanpa peduli huruf besar/kecil
        print(f"Jumlah {barang[0]}: {barang[1]}")
        break
else:
    print("Barang tidak ditemukan.")
    

# Memanggil fungsi tambah barang
stok_barang = tambah_barang(stok_barang)

# Memanggil fungsi hapus barang
hapus_barang()

# Memanggil fungsi urutkan barang
urutkan_barang()

# Memanggil fungsi tampilkan barang
tampilkan_barang()
exit()

#--------------------------------------Menghitung Total Pendapatan----------------------------------------
produk = [
    ["Sepatu", 600000, 10],
    ["Baju", 230000, 20],
    ["Kacamata", 750000, 5]
]

total = 0
for i in range(len(produk)):
    total += produk[i][1] * produk[i][2]
print(f"Total pendapatan: {total}")

#versi comprehension
total = sum([harga * jumlah for _, harga, jumlah in produk])
# for _, harga, jumlah in produk → langsung unpack elemen nested list.
# _ → nama produk (pakai _ artinya abaikan nilainya).
# harga * jumlah → hitung pendapatan per produk.
# sum([...]) → jumlahkan semua pendapatan.
print(f"Total pendapatan: {total}")

# versi lebih clean lagi tanpa tanda [] (pakai generator expression)
total = sum(harga * jumlah for _, harga, jumlah in produk)
print(f"Total pendapatan: {total}")
#-------------------------------------------------------------------------------------------------------
