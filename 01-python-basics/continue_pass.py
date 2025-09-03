#------------------------Melewati Angka Kelipatan 3 dalam Perulangan while------------------------
angka = 1
while angka <= 15:
    if angka % 3 == 0:
        angka += 1
        continue
    print(angka)
    angka += 1

exit()

#------------------------Lirik lagu------------------------
import time

# Daftar lirik dan durasi masing-masing baris (dalam detik)
lyrics_with_durations = [
    ("ubur ubur ikan", 1),
    ("i kan i ikan lele", 0.5),
    ("iiiii ikan lele", 0.5),
    ("iii kan kan kan kan lele", 0.5),
    ("ubur ubur ikan lele", 0.5),
    ("ikan ikan i ikan", 0.5),
    ("i i i i i ikan lele", 0.5),
    ("ikan lele ikan lele", 0.7),
    ("ubur ubur ikan", 0.6),
    ("ikan i ikan lele", 0.6),
    ("i i i i i ikan lele", 0.6),
    ("ikan kan kan kan ikan lele", 0.7),
    ("ubur ubur ikan lele", 0.5),
    ("ikan ikan i ikan", 0.5),
    ("i i i i i ikan lele", 0.5),
    ("ikan lele ikan lele", 0.5),
    ("ubur ubur ikan lele", 0.5),
]


# Durasi tampil setiap huruf (dalam detik)
char_duration = 0.1
# Durasi sebelum mulai menampilkan lirik (dalam detik)
intro_duration = 2

# Tunggu selama 'intro_duration' detik sebelum mulai
print("Memulai dalam {} detik...".format(intro_duration))
time.sleep(intro_duration)

# Menampilkan lirik per baris
for line, line_duration in lyrics_with_durations:
    for char in line:
        print(char, end='', flush=True)  # Menampilkan huruf tanpa pindah baris
        time.sleep(char_duration)  # Tunggu selama 'char_duration' detik
    print()  # Pindah ke baris berikutnya
    time.sleep(line_duration)  # Tunggu sesuai durasi untuk baris ini
print()
print()
exit()


#------------------------Melewati Huruf Vokal dalam Kata------------------------
huruf_vokal = "aiueoAIUEO"
kata = input("Masukkan kata: ")
hasil = ""

for huruf in kata:
    if huruf in huruf_vokal:
        continue
    hasil += huruf # Menambahkan huruf ke hasil jika bukan vokal
print("Kata tanpa huruf vokal: ", hasil)
exit()


#------------------------Melewati Bilangan Genap------------------------
for angka in range(1, 11):
    if angka % 2 == 0:
        continue #akan melewati angka genap
    print("Angka: ", angka)
exit()


#------------------------Melewati Angka Tertentu------------------------
for angka in range(1, 11):
    if angka == 5:
        continue #akan melewati angka 5
    print("Angka: ", angka)