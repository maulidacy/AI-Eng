#------------------------Menebak Angka------------------------.
import random
angka = random.randint(1, 20) # Komputer memilih angka acak dari 1 hingga 20
tebakan = None # Inisialisasi variabel untuk menyimpan tebakan

while tebakan != angka: # Loop berjalan terus
    tebakan = int(input("Tebakan Anda: "))
    if tebakan == angka:
        print("Selamat! Anda benar")
        break # Menghentikan loop jika tebakan == angka
    else:
        print("Maaf, Anda salah. Coba lagi!")
exit()



#------------------------Mencari Angka Tertentu------------------------
i = [2, 4, 6, 8, 10, 15, 20]

for angka in i:
    if angka > 10:
        print("Angka pertama yang lebih dari 10 adalah:", angka)
        break
