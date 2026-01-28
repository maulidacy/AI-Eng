name = input("Nama kamu: ")
kota = input("Kota asal kamu: ")
age_str = input("Umur kamu (angka): ")

age = int(age_str)

print(f"Halo, {name}!")
print(f"Kamu tinggal di {kota}.")
print(f"Tahun depan umur kamu: {age + 1}.")