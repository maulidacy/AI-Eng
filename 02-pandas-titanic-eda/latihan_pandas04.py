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

#-------------------------------------------Simpan Hasil Filter----------------------------------------------
print("\nSimpan Hasil Filter:")
df_jakarta = df[df["City"] == "Jakarta"]
print(df_jakarta)
#-------------------------------------------Filter Kombinasi lanjutan-------------------------------------------
print("\nFilter Kombinasi lanjutan:")
# Engineer di Jakarta dengan gaji > 8jt
df_eng_jkt = df[(df["Occupation"] == "Engineer") & (df["City"] == "Jakarta") & (df["Salary"] > 8000000)]
print(df_eng_jkt)
#------------------------------------------Filter OR (pilih salah satu kondisi)----------------------------------------
print("\nFilter OR (pilih salah satu kondisi):")
# Tinggal di Bandung ATAU usia > 25
df_subset = df[(df["City"] == "Bandung") | (df["Age"] > 25)]
print(df_subset)

#------------------------------------------Latihan----------------------------------------
print("\nBuat subnet df_jakarta yang hanya berisi orang Jakarta:")
df_jakarta = df[(df["City"] == "Jakarta")]
print(df_jakarta)

print("\nBuat subnet df_female yang hanya berisi orang Female:")
df_female = df[(df["Gender"] == "Female")]
print(df_female)
