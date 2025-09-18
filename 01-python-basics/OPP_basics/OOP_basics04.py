class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance  # protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}.")
        else:
            print("Invalid withdrawal amount.")

#======================================================================================================
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self._salary = salary   # protected (pakai underscore) privat

    def info(self):
        print("\n==== Informasi Karyawan ====")
        print(f"Nama: {self.name}")
        print(f"Umur: {self._age}")
        print(f"Gaji: {self._salary}")
        print("============================")
        
    def get_salary(self): # getter
        return self._salary

    def set_salary(self, new_salary): # setter
        if new_salary >= 0:
            self._salary = new_salary
            print(f"Gaji {self.name} diperbarui menjadi {self._salary}")
        else:
            print("❌ Gaji tidak boleh negatif!")
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 18:    
            self._age = new_age
        else:
            print("❌ Umur tidak boleh kurang dari 18!")
    def apply_raise(self, percent):
        self._salary += self._salary * percent / 100
        print(f"\nGaji {self.name} naik sebesar {percent}%. Update gaji baru:")

    employee_list = [] # class variable untuk menyimpan daftar karyawan

    def add_employee(self, employee):
        for employee in self.employee_list:
            if employee.name == self.name:
                print("❌ Karyawan sudah ada!")
                return
            else:
                self.employee_list.append(employee)
                print("✅ Karyawan berhasil ditambahkan!")

# Object object
emp1 = Employee("Maul", 20, 80000000)
emp2 = Employee("Yoo", 25, 70000000)

# Panggil Method
emp1.info()
emp2.info()
emp1.apply_raise(10) # Naikkan gaji 10%
emp1.info()

# Cetak gaji awal dengan get_salary()
print(f"Gaji awal {emp1.name}: {emp1.get_salary()}")
print(f"Gaji awal {emp2.name}: {emp2.get_salary()}")

# Ubah gaji dengan set_salary() → coba input angka positif & negatif.
emp1.set_salary(90000000) # Gaji baru
emp1.set_salary(-1000000)

# membandingkan langsung mengubah atribut _salary
emp1._salary = 50000000  # langsung ubah atribut _salary (bypass setter)
emp1.info()              # cek

# Periksa apakah atribut _salary benar-benar berubah.
emp1.info()

# Ubah age jadi protected (_age), lalu buat get_age() dan set_age().
# Validasi: umur tidak boleh < 18.