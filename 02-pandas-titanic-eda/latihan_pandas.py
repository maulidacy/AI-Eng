import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "Gender": ["Female", "Male", "Male", "Male", "Female"]
}

df = pd.DataFrame(data) # Membuat DataFrame dari dictionary, DataFrame adalah struktur data 2D seperti tabel
print(df) # Menampilkan DataFrame ke layar

#----------------------------------------------DASAR-------------------------------------------------
print("\n===========================================")
print("Menampilkan 3 baris pertama dari DataFrame:")
print("===========================================")
print(df.head(3)) # Menampilkan 3 baris pertama dari DataFrame

print("\n===========================================")
print("Informasi tentang DataFrame:")
print("===========================================")
print(df.info()) # Menampilkan informasi ringkas tentang DataFrame, termasuk tipe data dan jumlah nilai non-null

print("\n==============================================")
print("Dimensi DataFrame (jumlah baris, jumlah kolom):")
print("==============================================")
print(df.shape) # Menampilkan DataFrame dan dimensinya (jumlah baris dan kolom)

print("\n========================")
print("Hitung rata-rata usia:")
print("========================")
print(df["Age"].mean()) # Menghitung dan menampilkan rata-rata usia dari kolom "Age"


#----------------------------------------------Indexing and Filtering-------------------------------------------------


print("\n==============================")
print("Ambil semua data Gender male:")
print("==============================")
df_gender_male = df[df["Gender"] == "Male"] # Memfilter DataFrame untuk hanya menyertakan baris di mana kolom "Gender" bernilai "Male"
print(df_gender_male) # Menampilkan DataFrame yang sudah difilter

print("\n========================================")
print("Tambah kolom baru 'city':")
print("========================================")
df["City"] = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"] # Menambahkan kolom baru bernama "City" ke DataFrame
print(df) # Menampilkan DataFrame yang sudah diperbarui dengan kolom baru

print("\n================================")
print("Tambah kolom baru 'Occupation':")
print("================================")
df["Occupation"] = ["Engineer", "Doctor", "Artist", "Lawyer", "Scientist"] # Menambahkan kolom baru bernama "Occupation" ke DataFrame
print(df) # Menampilkan DataFrame yang sudah diperbarui dengan kolom baru

print("\n===============================")
print("Tambah kolom baru 'Salary':")
print("===============================")
df["Salary"] = [7000000, 4000000, 50000000, 9000000, 6000000] # Menambahkan kolom baru bernama "Salary" ke DataFrame
print(df) # Menampilkan DataFrame yang sudah diperbarui dengan kolom baru

#menampilkan nama kolom
print("\n========================")
print("Menampilkan nama kolom:")
print("========================")
print(df.columns) # Menampilkan nama-nama kolom dalam DataFrame

print("\n======================================")
print("Tampilkan isi kolom berdasarkan nama :")
print("======================================")
print(df["Name"]) # Menampilkan isi kolom "Name" dari DataFrame
print(df["City"]) # Menampilkan isi kolom "City" dari DataFrame
