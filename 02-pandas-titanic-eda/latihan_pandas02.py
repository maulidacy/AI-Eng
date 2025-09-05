import pandas as pd

# 1) Data mini untuk latihan (silakan ganti dengan data kamu)
data = {
    "Name": ["Ayu","Budi","Citra","Dodi","Eka","Fajar"],
    "Age":  [23,    31,    27,     22,    36,   29],
    "Gender":["Female","Male","Female","Male","Female","Male"],
    "City": ["Jakarta","Bandung","Jakarta","Surabaya","Jakarta","Bandung"],
    "Occupation":["Engineer","Designer","Engineer","Analyst","Manager","Engineer"],
    "Salary":[7000000, 5500000, 8200000, 4800000, 12000000, 9000000]
}
df = pd.DataFrame(data)

# Lihat data
print(df)

#----------------------------------------INDEXING (Ambil kolom/baris tertentu)----------------------------------------

# Kolom tunggal
names = df["Name"]

# Beberapa kolom
name_city = df[["Name","City"]]

# Baris pertama & terakhir (pakai iloc = index posisi)
first_row = df.iloc[0]
last_row  = df.iloc[-1]

# Baris ke-2 s.d. ke-4 (ingat: iloc eksklusif di ujung)
rows_2_to_4 = df.iloc[1:4]

#-----------------------------------------FILTERING (Seleksi baris pakai kondisi)----------------------------------------

age_over_25 = df[df["Age"] > 25]
female_only = df[df["Gender"] == "Female"]
salary_over_5m = df[df["Salary"] > 5_000_000]
eng_jkt = df[(df["Occupation"] == "Engineer") & (df["City"] == "Jakarta")]

#-----------------------------------------OPERASI KOLOM (Buat kolom baru, ubah, agregasi, sorting)----------------------------------------

# Pajak 10% dari gaji
df["Tax"] = df["Salary"] * 0.10

# Kelompok umur
def bucket_age(a):
    if a < 25: return "Young"
    if a <= 35: return "Adult"
    return "Senior"

df["Age_Group"] = df["Age"].apply(bucket_age)

#-----------------------------------------GROUPING (Agregasi per kategori)----------------------------------------
# Rata-rata, min, max gaji
avg_salary = df["Salary"].mean()
min_salary = df["Salary"].min()
max_salary = df["Salary"].max()

avg_salary_by_city = df.groupby("City")["Salary"].mean()
avg_salary_by_occ  = df.groupby("Occupation")["Salary"].mean()
count_by_gender    = df["Gender"].value_counts()
avg_age_by_occ     = df.groupby("Occupation")["Age"].mean()

#-----------------------------------------CHALLENGE (Latihan lanjutan)----------------------------------------
# 3 gaji tertinggi
top3_salary = df.nlargest(3, "Salary")

# Rata-rata gaji Engineer di Jakarta
avg_eng_jkt = df[(df["Occupation"]=="Engineer") & (df["City"]=="Jakarta")]["Salary"].mean()

# Total gaji per occupation
total_salary_by_occ = df.groupby("Occupation")["Salary"].sum()

# Urutkan gaji desc
sorted_by_salary = df.sort_values("Salary", ascending=False)

# Persentase jumlah orang per gender
pct_by_gender = (df["Gender"].value_counts(normalize=True) * 100).round(2)