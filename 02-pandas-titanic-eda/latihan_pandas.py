import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "Gender": ["Female", "Male", "Male", "Male", "Female"]
}

df = pd.DataFrame(data)
print(df)