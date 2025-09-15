class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def info(self):
        print("\n==== Informasi Karyawan ====")
        print(f"Nama: {self.name}")
        print(f"Umur: {self.age}")
        print(f"Gaji: {self.salary}")
        print("============================")

    def raise_salary(self, amount):
        self.salary += amount
        print(f"Gaji {self.name} naik sebesar {amount}. Gaji baru: {self.salary}")

    def is_senior(self):
        return self.age >= 30

# Object
emp1 = Employee("Maul", 20, 70000000)
emp2 = Employee("Budi", 35, 5500000)

# Panggil Method
emp1.info()
emp2.info()

emp1.raise_salary(500000) # Naikkan gaji emp1 sebesar 500000
emp1.info()

emp_list = [emp1, emp2] # List karyawan

# cek apakah senior
print(f"\n{emp1.name} senior: {emp1.is_senior()}")
print(f"{emp2.name} senior: {emp2.is_senior()}")    

# Versi if-else
if emp2.is_senior():
    print(emp2.name, "adalah karyawan senior")
else:
    print(emp2.name, "belum karyawan senior")