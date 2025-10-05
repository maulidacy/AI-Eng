from sklearn.datasets import load_iris
import pandas as pd

# load dataset
iris = load_iris(as_frame=True)
df = iris.frame

# lihat 5 baris pertama
print(df.head())

# cek jumlah sample tiap class
print(df['target'].value_counts())

# 