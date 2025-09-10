import pandas as pd

data = {
    "Name" : ["Ayu", "Budi", "Citra", "Ddodi", "Eka", "Fajar", "Gita", "Hadi"],
    "Age" : [23, 31, 27, 22, 36, 29, 24, 33],
    "Gender" : ["Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "City" : ["Jakarta", "Bandung", "Jakarta", "Surabaya", "Jakarta", "Bandung", "Jakarta", "Bandung"],
    "Occupation" : ["Engineer", "Designer", "Engineer", "Analyst", "Manager", "Engineer", "Designer", "Engineer"],
    "Salary" : [7000000, 5500000, 8200000, 4800000, 12000000, 9000000, 6000000, 7500000]    
}

df = pd.DataFrame(data)
print(df)

#-------------------------------------------Tambah Kolom Baru----------------------------------------------
# Pajak 10% dari gaji
df["Tax"] = df["Salary"] * 0.1
#-------------------------------------------Kolom dari Kondisi (pakai apply + lamda)----------------------------------------------
# Kelompok umur
df["Age_Group"] = df["Age"].apply(
    lambda x: "Young" if x < 25 else ("Adult" if x <= 35 else "Senior")
)
#-------------------------------------------Hapus Kolom----------------------------------------------
df.drop("Tax", axis=1, inplace=True) # hapus kolom Tax

#=========================================== LATIHAN 1 ==============================================

print("\nTambahkan kolom Tax = 10% dari kolom Salary:")
df["Tax"] = df["Salary"] * 0.1
print(df)

print("\nTambahkan kolom Net_Salary = Salary - Tax: ")
df["Net_Salary"] = df["Salary"] - df["Tax"]
print(df)

print("\nTambahkan kolom Age_Group:")
df["Age_Group"] = df["Age"].apply(
    lambda x: "Young" if x < 25 else ("Adult" if x <= 35 else "Senior")
)
print(df)

print("\nSimpan DataFrame ke file CSV:")
# df.to_csv("day5_result.csv", index=False)


#=========================================== LATIHAN 2 ==============================================
data_2 = {
    "Name": ["Ayu", "Budi", "Citra", "Dodi", "Eka"],
    "Age": [23, 31, 27, 22, 36],
    "Salary": [7000000, 5500000, 8200000, 4800000, 12000000]
}

df_2 = pd.DataFrame(data_2)
print(df_2)

#----------------------------------------- Transformasi Sederhana -----------------------------------------
# Tambah kolom Pajak (10% dari Salary) -> langsung rumus
df_2["Tax"] = df_2["Salary"] * 0.1

# Transformasi dengan Logika Bercabang
# tambah kolom Age_Group
df_2["Age_Group"] = df_2["Age"].apply(
    lambda x: "Young" if x < 25 else ("Adult" if x <= 35 else "Senior")
)

# Pakai Fungsi Biasa (alternatif lambda)
def categorize_age(x):
    if x < 25:
        return "Young"
    elif x <= 35:
        return "Adult"
    else:
        return "Senior"
    
df_2["Age_Group2"] = df["Age"].apply(categorize_age)

#----------------------------------------- Operasi String dengan apply -----------------------------------------
# Tambah kolom Nama_Lenght
df["Name_Length"] = df["Name"].apply(lambda x: len(x))
#----------------------------------------- Kondisi dengan Salary -----------------------------------------
# Tambah kolom Level: High kalau Salary > 8 juta, else Normal
df["Level"] = df["Salary"].apply(lambda x: "High" if x > 8000000 else "Normal")

#----------------------------------------- LATIHAN 3 -----------------------------------------