import pandas as pd

data = {
    "Name" : ["Ayu", "Budi", "Citra", "Ddodi", "Eka", "Fajar"],
    "Age" : [23, 31, 27, 22, 36, 29],
    "Gender" : ["Female", "Male", "Female", "Male", "Female", "Male"],
    "City" : ["Jakarta", "Bandung", "Jakarta", "Surabaya", "Jakarta", "Bandung"],
    "Occupation" : ["Engineer", "Designer", "Engineer", "Analyst", "Manager", "Engineer"],
    "Salary" : [7000000, 5500000, 8200000, 4800000, 12000000, 9000000]
}

df = pd.DataFrame(data)
print(df)