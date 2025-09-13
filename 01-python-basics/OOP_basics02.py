# Method = fungsi di dalam class
# Ditulis seperti fungsi biasa, tapi parameter pertamanya selalu self
# Bisa akses atribut object lewat self.atribut

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    # Method untuk menampilkan info karyawan
    def info(self):
        print(f"Nama: {self.name}, Umur: {self.age}, Gaji: {self.salary}")

    # Method untuk menghitung bonus
    def bonus(self, percent=10):
        total = self.salary + (self.salary * percent / 100)
        print(f"Gaji {self.name} setelah bonus {percent}% = {total}")

# Buat Object
emp1 = Employee("Ayu", 23, 7000000)
emp2 = Employee("Budi", 31, 5500000)

# Masukkan ke list setelah object dibuat
# emp_list = [emp1, emp2]

# Panggil Method
emp1.info()
emp2.info()
