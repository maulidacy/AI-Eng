import pandas as pd
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# 1. Buat DataFrame
data = {
    "nama": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "umur": [20, 22, 19, 21, 23],
    "nilai": [85, 90, 78, 60, 88]
}

df = pd.DataFrame(data)
logging.info("DataFrame dibuat dengan %d baris", len(df))
print("DataFrame awal:", df, sep="\n")

# 2. Tambahkan kolom baru
df["status"] = df["nilai"].apply(lambda x: "Lulus" if x >= 80 else "remidial")
logging.info("Kolom status ditambahkan")
print("DataFrame setelah menambahkan kolom status:", df, sep="\n")

# 3. Filter data (umur > 20)
df_filtered= df[df["umur"] > 20]
logging.info("Filter umur > 20 menghasilkan %d baris", len(df_filtered))
print("DataFrame setelah filter umur > 20:", df_filtered, sep="\n")

# 4. Hitung rata-rata nilai
avg = df["nilai"].mean()
logging.info("Rata-rata nilai: %.2f", avg)
print(f"Rata-rata nilai: {avg:.2f}")

# ----------------------------------------- CHALLENGE -----------------------------------------
# 1. Buat DataFrame dari dictionary
mahasiswa = {
    "nama": ["Andi", "Budi", "Citra", "Dewi", "Eka"],
    "jurusan": ["TI", "SI", "TI", "SI", "TI"],
    "ipk": [3.5, 3.8, 2.9, 3.2, 3.7]
}

