import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "Gender": ["Female", "Male", "Male", "Male", "Female"]
}

df = pd.DataFrame(data) # Membuat DataFrame dari dictionary, DataFrame adalah struktur data 2D seperti tabel
print(df) # Menampilkan DataFrame ke layar

print("\n===========================================")
print("Menampilkan 3 baris pertama dari DataFrame:")
print("===========================================")
print(df.head(3)) # Menampilkan 3 baris pertama dari DataFrame

print("\n===========================================")
print("Informasi tentang DataFrame:")
print("===========================================")
print(df.info()) # Menampilkan informasi ringkas tentang DataFrame, termasuk tipe data dan jumlah nilai non-null
