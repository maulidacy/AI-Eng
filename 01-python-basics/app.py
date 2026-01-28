name = input("Nama kamu: ")
kota = input("Kota asal kamu: ")
age_str = input("Umur kamu (angka): ")

age = int(age_str)  # ubah teks jadi angka
print("Halo,", name)
print("Kamu tinggal di", kota)
print("Tahun depan umur kamu:", age + 1)