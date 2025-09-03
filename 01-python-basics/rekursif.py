#------------------------Fibonacci (Dasar - Menengah)------------------------
def fibonacci(n):
    if n < 0:
        raise ValueError("Indeks tidak boleh negatif") # Mengangkat kesalahan jika n negatif
    elif n == 0:
        return 0 # Bilangan Fibonacci ke-0 adalah 0
    elif n == 1:
        return 1 # Bilangan Fibonacci ke-1 adalah 1
    else:
        # Menghitung Fibonacci dengan pemanggilan rekursif
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    n = int(input("Input n : "))
    result = fibonacci(n) # Memanggil fungsi untuk menghitung Fibonacci ke-n
    print(f"Bilangan Fibonacci ke-{n} adalah {result}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}") # Menangkap dan mencetak kesalahan jika terjadi
exit()



#------------------------Chatbot Sederhana dengan Balasan Bertingkat------------------------
def chatbot(input_pengguna):
    input_pengguna = input("Apa yang ingin Anda tanyakan? ")
    if input_pengguna == "harga":
        input_pengguna = input("Produk apa? ")
    elif input_pengguna == "kue bulan":
        print("Harga kue bulan Rp. 45.000/pax ")
    elif input_pengguna == "kue lapis":
        print("Harga kue lapis Rp. 30.000/pax ")
    else:
        input_pengguna = input("Maaf, saya tidak mengerti pertanyaan Anda. ")
        return input_pengguna
    
chatbot("harga?")
exit()

#------------------------Sistem Kasir (Hitung Total Harga dengan Diskon Bertingkat)------------------------
def hitung_total(harga):
    if harga >= 500000:
        diskon = 0.1 * harga
        return harga - diskon
    elif harga >= 1000000:
        diskon = 0.15 * harga
        return harga - diskon
    else:
        diskon = 0.2 * harga
        return harga - diskon

print(hitung_total(1200000))  # Output: Total setelah diskon
print(hitung_total(700000))
exit()



#------------------------Struktur Folder dan File (Recursive File Explorer)------------------------
def tampilkan_folder(folder, level=0):
    """Menampilkan isi folder dan file secara rekursif"""
    for key, value in folder.items():
        print("   " * level + "📂 " + key)  # Cetak nama folder

        if isinstance(value, dict):  # Jika isinya folder, panggil rekursi
            tampilkan_folder(value, level + 1)
        elif isinstance(value, list):  # Jika isinya list (file), cetak file-nya
            for file in value:
                if file.endswith((".jpg", ".png")):
                    icon = "🖼️"
                else:
                    icon = "📄"
                print("   " * (level + 1) + f"{icon} {file}")

# Contoh Data
data = {
    "Project": {
        "Documents": ["file1.txt", "file2.docx"],
        "Images": ["photo1.jpg", "photo2.png"]
    }
}

# Jalankan fungsi
tampilkan_folder(data)

exit()



#------------------------Menghitung Pajak Berlapis (Progressive Tax)------------------------
def hitung_pajak(pendapatan):
    if pendapatan <= 5000000:
        return 0.05 * pendapatan
    elif pendapatan <= 10000000:
        return (5000000 * 0.05) + ((pendapatan - 5000000) * 0.10)
    else:
        return (5000000 * 0.05) + (5000000 * 0.10) + ((pendapatan - 10000000) * 0.15)

pendapatan1 = 12000000
pendapatan2 = 8000000

print(f"Pajak untuk pendapatan {pendapatan1}: Rp {hitung_pajak(pendapatan1):,.0f}")
print(f"Pajak untuk pendapatan {pendapatan2}: Rp {hitung_pajak(pendapatan2):,.0f}")

exit()

#------------------------Mencari Nilai Maksimum dalam List------------------------
def cari_maksimum(lst):
    return max(lst) #Mencari Nilai Minimum dalam List

def cari_minimum(lst):
    return min(lst) #Mengurutkan List dalam Urutan Ascending

def urut_asc(lst):
    return sorted(lst) #Mengurutkan List dalam Urutan Descending

def urut_desc(lst):
    return sorted(lst, reverse=True)

print(cari_maksimum([3, 1, 8, 2, 5]))  # Output: 8
print(cari_maksimum([10, 20, 5, 30, 25]))  # Output: 30

exit()

#------------------------Jumlahkan Digit dalam Bilangan------------------------
def jumlahkan_digit(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + jumlahkan_digit(n // 10) # Mengembalikan jumlah digit n dengan menambahkan digit terakhir (n % 10) dan hasil jumlah digit dari sisa bilangan (n // 10).

print(jumlahkan_digit(1234))
print(jumlahkan_digit(5678))

exit()


#------------------------Hitung Total Digit------------------------
def hitung_digit(n):
    if n == 0: # Jika n adalah 0, jumlah digitnya adalah 0
        return 0
    else:
        return 1 + hitung_digit(n // 10)  # Jika n lebih besar dari 0, tambahkan 1 dan panggil rekursi dengan n dibagi 10
    
print(hitung_digit(12345))
print(hitung_digit(987654))
exit()



#------------------------Buat fungsi rekursif untuk membalik string------------------------
def balik_string(teks):
    if len(teks) == 0:
        return teks
    else:
        return balik_string(teks[1:]) + teks[0]
print(balik_string("hello"))
exit()



#------------------------fungsi rekursif untuk menghitung jumlah angka dari 1 hingga n------------------------
def hitung_jumlah_angka(n):
    if n == 1:
        return 1 #Jika n sama dengan 1, fungsi mengembalikan 1. Ini mencegah rekursi berlanjut selamanya.
    else:
        return n + hitung_jumlah_angka(n-1) #Jika n lebih besar dari 1, fungsi mengembalikan nilai n ditambah hasil dari pemanggilan fungsi itu sendiri dengan argumen n - 1
    
n = 5
hasil = hitung_jumlah_angka(n)
print(hasil)

exit()


#------------------------Pangkat------------------------
def pangkat(a,b): #mendefinisikan sebuah fungsi bernama pangkat yang menerima dua argumen, yaitu a dan b
    return a ** b #mengembalikan hasil dari a dipangkatkan dengan b. Operator ** digunakan untuk menghitung pangkat
hasil = pangkat(2, 3) #memanggil fungsi pangkat dengan 2 sebagai a dan 3 sebagai b. Hasil dari fungsi ini (yaitu 2 ** 3, yang sama dengan 8) disimpan dalam variabel hasil
print(hasil)