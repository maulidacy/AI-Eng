import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "Gender": ["Female", "Male", "Male", "Male", "Female"]
}

df = pd.DataFrame(data) # Membuat DataFrame dari dictionary, DataFrame adalah struktur data 2D seperti tabel
print(df) # Menampilkan DataFrame ke layar
#-------------------------- Load DataFrame dari CSV -------------------------
# df = pd.read_csv("titanic.csv") # Membaca data dari file CSV dan menyimpannya dalam DataFrame
# print(df) # Menampilkan DataFrame ke layar

#--------------------------Series-------------------------
s = pd.Series([10, 20, 30], index=["a", "b", "c"]) # Membuat Series dari list dengan index khusus
print(s) # Menampilkan Series ke layar
print("Ambil elemen b:", s["b"]) # Mengambil elemen dengan index "b" dari Series
exit()

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


#----------------------------------------------INDEXING-------------------------------------------------


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
df["Occupation"] = ["Engineer", "Doctor", "Engineer", "Lawyer", "Scientist"] # Menambahkan kolom baru bernama "Occupation" ke DataFrame
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

print("\n=================================")
print("Ambil baris pertama dan terakhir:")
print("=================================")
print(df.iloc[[0, -1]]) # Mengambil dan menampilkan baris pertama dan terakhir dari DataFrame (iloc itu index location)

print("\n=================================")
print(df.iloc[1:5]) # Menggunakan Range untuk Mengambil dan menampilkan baris ke 2 sampai 4 (index 1 sampai 3) dari DataFrame


#----------------------------------------------FILTERING-------------------------------------------------


print("\n===================================")
print("Ambil semua orang dengan usia > 25:")
print("===================================")
df_age_above_25 = df[df["Age"] > 25] # Memfilter DataFrame untuk hanya menyertakan baris di mana kolom "Age" lebih besar dari 25
print(df_age_above_25) # Menampilkan DataFrame yang sudah difilter

print("\n=================================")
print("Ambil semua orang gender female:")
print("=================================")
df_gender_female = df[df["Gender"] == "Female"] # Memfilter DataFrame untuk hanya menyertakan baris di mana kolom "Gender" bernilai "Female"
print(df_gender_female) # Menampilkan DataFrame yang sudah difilter

print("\n==========================================")
print("Ambil semua orang dengan Salary > 5000000:")
print("==========================================")
df_salary_above_5000000 = df[df["Salary"] > 5000000] # Memfilter DataFrame untuk hanya menyertakan baris di mana kolom "Salary" lebih besar dari 5000000
print(df_salary_above_5000000) # Menampilkan DataFrame yang sudah difilter

print("\n===================================================================")
print("Ambil semua orang dengan Occupation 'Engineer' dan City 'New York':")
print("===================================================================")
df_engineer_in_newyork = df[(df["Occupation"] == "Engineer") & (df["City"] == "New York")] # Memfilter DataFrame untuk hanya menyertakan baris di mana kolom "Occupation" bernilai "Engineer" dan kolom "City" bernilai "New York"
print(df_engineer_in_newyork) # Menampilkan DataFrame yang sudah difilter

#----------------------------------------------OPERASI KOLOM-------------------------------------------------

print("\n===================================")
print("Tambah kolom Tax (10% dari Salary):")
print("====================================")
df["Tax"] = df["Salary"] * 0.1 # Menambahkan kolom baru bernama "Tax" yang merupakan 10% dari kolom "Salary"
print(df) # Menampilkan DataFrame yang sudah diperbarui dengan kolom baru

print("\n=============================================")
print("Tambah kolom Age_Group (Young, Adult, Senior:")
print("=============================================")
# Menambahkan kolom baru 'age_group'
df["Age_Group"] = df["Age"].apply(
    lambda x: "Young" if x < 25 else ("Adult" if x <= 35 else "Senior")
    )
print(df) # Menampilkan DataFrame yang sudah diperbarui dengan kolom baru

# versi lebih gampang dibaca, bisa juga ditulis tanpa lambda:
# Fungsi untuk mengelompokkan umur
def kategori_umur(x):
    if x < 25:
        return "Young"
    elif x <= 35:
        return "Adult"
    else:
        return "Senior"

# Tambahkan kolom 'age_group' dengan apply
df["age_group"] = df["Age"].apply(kategori_umur)
# print(df) # Menampilkan DataFrame yang sudah diperbarui dengan kolom baru

print(f"\nRata-rata gaji: {df['Salary'].mean()}") # Menampilkan rata-rata gaji ke layar
print(f"Salary tertinggi: {df['Salary'].max()}") # Menampilkan gaji tertinggi ke layar
print(f"Salary terendah: {df['Salary'].min()}") # Menampilkan gaji terendah ke layar


print("\n==================================")
print("Rata-rata salary berdasarkan city:")
print("==================================")
avg_salary_by_city = df.groupby("City")["Salary"].mean() # Mengelompokkan DataFrame berdasarkan kolom "City" dan menghitung rata-rata dari kolom "Salary" untuk setiap kota
print(avg_salary_by_city) # Menampilkan rata-rata gaji berdasarkan kota

print("\n========================================")
print("Rata-rata salary berdasarkan occupation:")
print("========================================")
avg_salary_by_occupation = df.groupby("Occupation")["Salary"].mean() # Mengelompokkan DataFrame berdasarkan kolom "Occupation" dan menghitung rata-rata dari kolom "Salary" untuk setiap pekerjaan
print(avg_salary_by_occupation) # Menampilkan rata-rata gaji berdasarkan pekerjaan

print("\n=================================")
print("Jumlah orang berdasarkan Gender:")
print("=================================")
count_by_gender = df.groupby("Gender").size() # Mengelompokkan DataFrame berdasarkan kolom "Gender" dan menghitung jumlah baris untuk setiap jenis kelamin
print(count_by_gender) # Menampilkan jumlah orang berdasarkan jenis kelamin

print("\n=============================")
print("Rata-rata Age per occupation:")
print("=============================")
print(df.groupby("Occupation")["Age"].mean()) # Mengelompokkan DataFrame berdasarkan kolom "Occupation" dan menghitung rata-rata dari kolom "Age" untuk setiap pekerjaan

print("\n=================================")
print("3 orang dengan Salary tertinggi:")
print("=================================")
top_3_salary = df.nlargest(3, "Salary") # Mengambil 3 baris dengan nilai tertinggi di kolom "Salary"
print(top_3_salary) # Menampilkan 3 orang dengan gaji tertinggi

print("\n============================================================")
print("Total salary yang harus dibayar perusahaan tiap occupation:")
print("============================================================")
total_salary_by_occupation = df.groupby("Occupation")["Salary"].sum() # Mengelompokkan DataFrame berdasarkan kolom "Occupation" dan menghitung total dari kolom "Salary" untuk setiap pekerjaan
print(total_salary_by_occupation) # Menampilkan total gaji yang harus dibayar perusahaan untuk setiap pekerjaan

print("\n=============================================================")
print("DataFrame diurutkan berdasarkan salary tertinggi ke terendah:")
print("=============================================================")
sorted_by_salary = df.sort_values(by="Salary", ascending=False) # Mengurutkan DataFrame berdasarkan kolom "Salary" dari yang tertinggi ke terendah
print(sorted_by_salary) # Menampilkan DataFrame yang sudah diurutkan berdasarkan gaji

print("\n===========================================")
print("Persentase jumlah orang berdasarkan Gender:")
print("===========================================")
percentage_by_gender = df.groupby("Gender").size() / len(df) * 100 # Menghitung persentase jumlah orang berdasarkan jenis kelamin
print(percentage_by_gender) # Menampilkan persentase jumlah orang berdasarkan jenis kelamin




