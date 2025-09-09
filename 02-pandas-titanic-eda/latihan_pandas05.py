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