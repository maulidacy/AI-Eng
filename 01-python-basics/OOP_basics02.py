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

    # Static Method untuk net salary semua karyawan
    @staticmethod  # @staticmethod artinya method ini tidak butuh self (tidak terikat pada 1 object)
    def net_salary(emp_list, tax=5):
        for emp in emp_list:  # gunakan for untuk menghitung semua karyawan dalam emp_list
            net = emp.salary - (emp.salary * tax / 100)
            print(f"Gaji bersih {emp.name} setelah pajak {tax}% = {net}")

    @staticmethod
    def change_name(emp_list, new_name):
        for emp in emp_list:
            emp.name = new_name
            print(f"Nama diubah menjadi: {emp.name}")

# Buat Object
emp1 = Employee("Ayu", 23, 7000000)
emp2 = Employee("Budi", 31, 5500000)

# Masukkan ke list setelah object dibuat
emp_list = [emp1, emp2]  # Kalau banyak karyawan gunakan list

# Panggil Method
emp1.info()
emp2.info()

emp1.bonus(15)   # contoh menghitung bonus 15%
emp2.bonus()     # default bonus 10%

emp1.change_name("Ayu Lestari")  # Panggil method untuk ganti nama
emp2.change_name("Budi Santoso")    

# Panggil method statis dengan passing list
Employee.net_salary(emp_list, tax=5)

Employee.change_name(emp_list, "Karyawan")  # Ganti semua nama karyawan jadi "Karyawan
