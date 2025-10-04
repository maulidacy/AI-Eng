from sklearn.datasets import load_iris
import pandas as pd

# load dataset
iris = load_iris(as_frame=True)
df = iris.frame

print(df.head())