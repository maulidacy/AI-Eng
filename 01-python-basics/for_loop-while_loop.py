# In coding and business

#-------------------------------------------------menghitung bilangan terbesar------------------------------------------------
list_bilangan = []

while True:
    bilangan = input("Masukkan bilangan (atau ketik 'selesai' untuk berhenti): ")
    if bilangan.lower() == "selesai":
        max_bilangan = max(list_bilangan)
        print("Bilangan terbesar: ", max_bilangan)
        break
    else:
        list_bilangan.append(int(bilangan)) #tambah bilangan ke list, int() untuk mengubah string jadi integer
        print("List bilangan: ", list_bilangan)
exit()

#---------------------------------------------menghitung huruf vokal------------------------------------------------
kata = input("Masukkan kata: ")
vokal = ["a", "i", "u", "e",]
hitung = 0

for huruf in kata:
    if huruf in vokal:
        hitung += 1

print("Jumlah huruf vokal:", hitung)
exit()

#---------------------------------------------------------------------------------------------
teks = "AI itu seru banget"
for huruf in teks.split():
    print(huruf)
exit()

#-------------------------- Cek Password ----------------------------------------------------
password = "rahasia"
input_password = ""

while input_password != password:
    input_password = input("Masukkan password: ")
    if input_password == password:
        print("Akses diterima!")
    else:
        print("Akses ditolak!")
exit()

#---------------------------------------------------------------------------------------------
x = 1

while x <=5:
    print(x)
    x += 1
exit()
#---------------------------- itung jumlah angka dalam list ----------------------------------
angka = [3, 5, 7, 9, 2]
jumlah_total_angka = 0
for i in angka:
    jumlah_total_angka += i
print(f"Jumlah total angka: {jumlah_total_angka}")
exit()
#---------------------------------------------------------------------------------------------
n = 20

for i in range(1, n + 1):  # Loop dari angka 1 sampai 20 (range(1, 21), karena n + 1 = 21 → akhir range tidak termasuk).
    if i % 2 == 0:
        print(f"{i}", end=" ")
exit()

#---------------------------------------------------------------------------------------------
for i in range (1, 11): 
    print(f"{i}", end=" ")  # Mencetak angka 1 sampai 10 dalam satu baris, dipisahkan spasi.
exit()
#-------------------------- 8. Jumlahkan angka hingga total ≥ 100, Hentikan jika total sudah ≥ 100.--------------------------
jumlahAngka = 100
angka = 0
total = 0

while total != jumlahAngka:
    angka = int(input("Masukkan angka: "))
    total += angka
    if total == jumlahAngka:
        print("Total mencapai 100, program selesai.")
    elif total > jumlahAngka:
        print("Total melebihi 100, program selesai.")
        break
    else:
        print(f"Total saat ini: {total}, masukkan angka lagi.")
exit()

#-------------------------- 7. Input sampai benar --------------------------
angka = 5
tebakan = 0 

while tebakan != 5:
    tebakan = int(input("Masukkan angka: "))
    if tebakan == angka:
        print("Benar!")
        break
    elif tebakan != angka:
        print("Salah!") 
exit()

#-------------------------- 6. Hitung mundur dari 10 ke 1 --------------------------
i = 10
while i >= 1: 
    print(i) 
    i -= 1
exit()

#-------------------------- 5. Hitung jumlah huruf vokal dalam sebuah kata atau kalimat -------------------------
hurufVokal = "aeiouAEIOU"
jumlah_huruf = 0
kataOrKalimat = input("Masukkan kata atau kalimat: ")

for i in kataOrKalimat:
    if i in hurufVokal:
        jumlah_huruf += 1
print(f"Jumlah huruf vokal: {jumlah_huruf}")
exit()

#------------------------- 4. Cetak segitiga bintang -------------------------
n = int(input("Masukkan n: "))
for i in range(1, n + 1):
    print('*' * i)  # Mencetak bintang sebanyak i kali, menghasilkan pola segitiga.
exit()

#------------------------- 3. Hitung jumlah bilangan dari 1 sampai 100 -------------------------
jumlahBilangan = 0
n = 100

for i in range(1, n + 1):
    jumlahBilangan += i
    print(f"Jumlah: {jumlahBilangan}")
exit()

#------------------------- 2. Tampilkan angka genap dari 1 sampai 20 -------------------------
jumlah_genap = 0
print("Angka genap:", end=" ")
n = 20  # batas atas

for i in range(1, n + 1): # Loop dari angka 1 sampai 20 (range(1, 21), karena n + 1 = 21 → akhir range tidak termasuk).
    if i % 2 == 0:
        print(i, end=" ") # Mencetak tulisan "Angka genap:" di awal baris, tanpa ganti baris (end=" ").
        jumlah_genap += 1

print()
print("Jumlah angka genap:", jumlah_genap)
exit()

#------------------------- 1. Cetak angka 1 sampai 10 -------------------------
for i in range(1, 11):
    print(i)