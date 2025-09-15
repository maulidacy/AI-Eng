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