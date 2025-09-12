# Class = template (cetakan)
# Object = instance dari class
# Method = fungsi/aksi yang ada di dalam class
# Attribute = variabel, data tiap object

# Class Employee (definisi umum -> template)

#------------------------------------------class dengan Atribut & Method Dasar----------------------------------
# Hanya definisi perlu buat object dari class untuk digunakan
class Employee:
    def __init__(self, name, age, salary): # constructor
        self.name = name
        self.age = age
        self.salary = salary

    def info(self): # method
        print(f"Nama: {self.name}, Umur: {self.age}, Gaji: {self.salary}")

    def bonus(self, percent=10):
        total = self.salary + (self.salary * percent / 100)
        print(f"Gaji {self.name} setelah bonus {percent}% = {total}")

# Gunakan Class
# Buat object
emp1 = Employee("Ayu", 23, 7000000) # constructor dipanggil otomatis
emp2 = Employee("Budi", 31, 5500000)

# Panggil method
emp1.info()
emp2.info()

# Hitung bonus
emp1.bonus() #default 10%
emp2.bonus(15) #bonus 20%



#------------------------------------------CONSTRUCTOR------------------------------------------
class Employeee:
    def __init__(self, name, age, salary): # constructor
        self.name = name
        self.age = age
        self.salary = salary

# saat emp1 dibuat, constructor langsung jalan -> atribut name, age, salary terisi
emp1 = Employeee("Ayu", 23, 7000000) # constructor dipanggil otomatis

# tanpa constructor, harus diisi secara manual
# emp1 = Employee()
# emp1.name = "Ayu"
# emp1.age = 23
# emp1.salary = 7000000 

#------------------------------------------LATIHAN------------------------------------------
print("\nLatihan OOP")
class EmployeeSederhana:
    def __init__(self, name, age, salary, department):   # constructor
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def info(self):   # method
        print(f"Nama: {self.name}, Umur: {self.age}, Gaji: {self.salary}, Department: {self.department}")

# Buat Object
emp1 = EmployeeSederhana("Ayu", 23, 7000000, "IT")
emp2 = EmployeeSederhana("Budi", 31, 5500000, "HR")

# Panggil Method
emp1.info()
emp2.info()



