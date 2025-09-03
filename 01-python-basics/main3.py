#-------------------------Konversi Mata Uang-------------------------
# Fungsi untuk mengonversi Rupiah ke USD dan Euro
def konversi_rupiah(rupiah):
    kurs_usd = 15500
    kurs_euro = 17000
    
    # Menghitung konversi
    usd = rupiah / kurs_usd
    euro = rupiah / kurs_euro
    
    return usd, euro

# Input dari pengguna
jumlah_rupiah = float(input("Masukkan jumlah uang dalam Rupiah: "))

# Melakukan konversi
usd, euro = konversi_rupiah(jumlah_rupiah)

# Menampilkan hasil
print(f"{jumlah_rupiah} Rupiah setara dengan {usd:.2f} USD atau {euro:.2f} Euro.")
exit()



#-------------------------Hitung Waktu Perjalanan-------------------------
jarak = float(input("Masukkan jarak perjalanan (km): "))
kecepatan = float(input("Masukkan kecepatan rata-rata (km/jam): "))
waktu = jarak / kecepatan

print(f"Perjalanan akan memakan waktu sekitar {waktu:.2f} jam.")
exit()


#-------------------------Penilaian Ujian Mahasiswa (For Loop)-------------------------
print(25*"=")
print("Penilaian Ujian Mahasiswa")
print(25*"=" + "\n")

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah_mahasiswa):
    nilai = float(input(f"Masukkan nilai mahasiswa ke-{i + 1}: "))
    if nilai >= 60 and nilai <= 100:
        print(f"Mahasiswa ke-{i + 1}: Lulus")
    else:
        print(f"Mahasiswa ke-{i + 1}: Tidak Lulus")
exit()


#-------------------------Penjualan Tiket Konser (While Loop)-------------------------
print(25*"=")
print("Penjualan Tiket Konser")
print(25*"=" + "\n")

tiket_tersedia = 100
tiket_sisa = 0

print(f"Tiket tersedia: {tiket_tersedia}")

while True:
    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
    if jumlah_tiket <= tiket_tersedia:
        tiket_sisa = tiket_tersedia - jumlah_tiket
        tiket_tersedia = tiket_sisa
        print(f"Tiket berhasil dibeli. Sisa tiket: {tiket_tersedia}")
    else:
        print("Maaf, tiket habis!")
        break

exit()



#-------------------------Simulasi ATM (While Loop)-------------------------
print(13*"=")
print("Simulasi ATM")
print(13*"=" + "\n")

print("1. Cek Saldo")
print("2. Tarik Uang")
print("3. Keluar")
print()

saldo = 1000000

while True:
    menu = int(input("Pilih menu: "))
    if menu == 1:
        print(f"Saldo Anda: Rp. {saldo}")
    elif menu == 2:
        penarikan = float(input("Masukkan jumlah penarikan: Rp."))
        print("Penarikan berhasil! Sisa saldo: RP. ", saldo - penarikan)
    elif menu == 3:
        print("Terima kasih telah menggunakan layanan ATM.")
        break
    else:
        print("Menu tidak tersedia. Silakan pilih menu lainnya.")
exit()

#-------------------------Pemesanan Tiket Bioskop (While Loop)-------------------------
print(20*"=")
print("Pemesanan Tiket Bioskop")
print(20*"=" + "\n")

harga_pertiket = 50000
total_harga = 0
jumlah_tiket = 0

while True:
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))
    if jumlah_tiket <= 0:
        print("Terima kasih telah membeli tiket!")
        break
    total_harga = harga_pertiket * jumlah_tiket
    print(f"Total harga: {total_harga}")

exit()



#-------------------------Pengelolaan Stok Barang (For Loop)-------------------------
print(20*"=")
print("Pengelolaan Stok Barang")
print(20*"=" + "\n")

jumlah_barang = int(input("Masukkan jumlah barang: ")) 

barang_list = []
for i in range(jumlah_barang):
    barang = input(f"Masukkan nama barang ke-{i + 1}: ")
    barang_list.append(barang)

print("\nDaftar barang di gudang:")
for i in range(len(barang_list)): # len(barang_list) Mengembalikan jumlah elemen dalam barang_list. 
    print(f"{i + 1}. {barang_list[i]}")
exit()


#-------------------------Konversi Suhu (For Loop)-------------------------
print(15*"=")
print("Konversi Suhu")
print(15*"=" + "\n")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

jumlah_suhu = int(input("Masukkan jumlah suhu: "))

suhu_list = [] # Menyimpan suhu yang dimasukkan
for i in range(jumlah_suhu):
    suhu = float(input(f"Masukkan suhu ke-{i + 1} (C): "))
    suhu_list.append(suhu) # menambahkan nilai suhu yang dimasukkan oleh pengguna ke dalam daftar suhu_list.

print("\nHasil konversi:")
for suhu in suhu_list:
    fahrenheit = celsius_to_fahrenheit(suhu)
    print(f"{int(suhu)}C = {int(fahrenheit)}F") # Menggunakan int() untuk mengonversi hasil ke integer
exit()


#-------------------------Mesin Parkir (While Loop)-------------------------
print(15*"=")
print("Mesin Parkir")
print(15*"=" + "\n")

tarif_per_jam = 5000
biaya_parkir = 0
total_pembayaran = 0

while True:
    jumlah_jam = float(input("Masukkan jumlah jam parkir: "))
    biaya_parkir = jumlah_jam * tarif_per_jam
    total_pembayaran += biaya_parkir
    print(f"Biaya parkir: Rp {biaya_parkir}")
    perintah = input("Ketik 'keluar' untuk berhenti atau tekan enter untuk lanjut: ")
    if perintah.lower() == "keluar": #lower() digunakan untuk mengubah semua huruf dalam string menjadi huruf kecil.
        print(f"Total pembayaran: {total_pembayaran}")
        break
exit()


#-------------------------Menghitung Rata-rata Nilai Siswa (For Loop)-------------------------
print(35*"=")
print("Menghitung Rata-rata Nilai Siswa")
print(35*"=" + "\n")

jumlah_siswa = int(input("Masukkan jumlah siswa: "))
total_nilai = 0

for i in range(jumlah_siswa):
    nilai = float(input(f"Masukkan nilai siswa ke-{i + 1}: "))
    total_nilai += nilai
    rata_rata = total_nilai / jumlah_siswa
print(f"Rata-rata nilai kelas: {rata_rata}")

exit()


#-------------------------Sistem Login dengan Batas Percobaan (While Loop)-------------------------
print(35*"=")
print("Sistem Login dengan Batas Percobaan")
print(35*"=" + "\n")

username = "admin"
password = 1234
input_username = input("Masukkan username: ")
kesempatan = 3


while kesempatan > 0:
    input_password = input("Masukkan password: ")
    if input_username == username and input_password == str(password):
        print("Login berhasil! Selamat datang.")
        break
    elif input_username == username and input_password != password:
        kesempatan -= 1
        print(f"Password salah! {kesempatan} percobaan tersisa.")
if kesempatan == 0: # Memeriksa apakah kesempatan telah habis.
    print("Maaf kesempatan habis. Akun terkunci!")
exit()


#-------------------------Kalkulator Total Belanja (For Loop)-------------------------
print(25*"=")
print("Kalkulator Total Belanja")
print(25*"=" + "\n")

jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = 0

for i in range(jumlah_barang):
    harga = int(input(f"Masukkan harga barang ke-{i + 1}: "))
    total_harga += harga
print(f"Total harga belanjaan: {total_harga}")

exit()