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

#-------------------------------------------LATIHAN----------------------------------------------
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

# Tanpa inplace
df2 = df.drop("Tax", axis=1)   # hasil disimpan ke df2
print(df.columns)              # Tax masih ada

# Dengan inplace
df.drop("Tax", axis=1, inplace=True)  # langsung ubah df
print(df.columns)              # Tax sudah hilang
print("\nHapus kolom Tax:")
df.drop("Tax", axis=1, inplace=True) # hapus kolom Tax
print(df)

print("\nSimpan DataFrame ke file CSV:")
df.to_csv("day5_result.csv", index=False)