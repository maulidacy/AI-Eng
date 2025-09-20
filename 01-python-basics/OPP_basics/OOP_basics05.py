#========================================== Inheritance ==========================================
# Inheritance = pewarisan atribut & method dari class induk (superclass) ke class anak (subclass).
# Tujuannya: hierarki class + code reusability.

# Parent class (superclass)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"{self.name}, gaji: {self.salary}")
    
    def bonus(self, amount):
        self.salary += amount
        print(f"Gaji {self.name} setelah bonus: {self.salary}")

# Child class (subclass)
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    # Override method
    def info(self):
        print(f"{self.name}, gaji: {self.salary}, memimpin tim: {self.team_size} orang")

class Intern(Employee):
    def __init__(self, name, salary, duration):
        super().__init__(name, salary)
        self.duration = duration  # dalam bulan

    # Override method
    def info(self):
        print(f"{self.name}, gaji: {self.salary}, status: intern selama {self.duration} bulan")

    # Override bonus method
    def bonus(self, amount):
        # misal intern hanya boleh dapat setengah dari bonus
        self.salary += amount / 2
        print(f"Gaji {self.name} setelah bonus (intern): {self.salary}")

class Engineer(Employee):
    def __init__(self, name, salary, langs=None):
        super().__init__(name, salary)
        self.langs = langs if langs else []

    def languages(self):
        if self.langs:
            print(f"{self.name} menguasai bahasa {', '.join(self.langs)}") # ", ".join(langs) = menggabungkan list jadi string dipisahkan koma

        else:
            print(f"{self.name} belum menambahkan bahasa yang dikuasai")

# Buat objek dari kelas Employee
emp1 = Employee("Alice", 7000000)
emp1.info()

# Buat objek dari class Manager
mgr1 = Manager("Yoo", 10000000, 5)
mgr1.info()

# method bonus dari class Employee
emp1.bonus(500000)

# Buat objek dari class Engineer
eng1 = Engineer("Bob", 8000000, ["Python", "JavaScript"])
eng1.info()
eng1.languages()

# Buat list employees
employees = [
    Manager("Charlie", 12000000, 10),       # Manager
    Engineer("David", 9000000, ["Python"]), # Engineer
    Engineer("Eva", 6000000, ["Java"]),     # Engineer
    Intern("Eve", 3000000, 6)               # Intern
]

# Loop semua karyawan
for emp in employees:
    emp.info()  # Panggil method info() sesuai class masing-masing
    if isinstance(emp, Engineer):
        emp.languages()  # Panggil method languages() hanya untuk Engineer
