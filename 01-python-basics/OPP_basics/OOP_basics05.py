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
        super().__init__(name, salary) # panggil constructor parent class
        self.team_size = team_size

    # Override method
    def info(self):
        print(f"{self.name}, gaji: {self.salary}, memimpin tim: {self.team_size} orang")

class Intern(Employee):
    def bonus(self, amount):
        # misal intern hanya boleh dapat setengah dari bonus
        self.salary += amount / 2
        print(f"Gaji {self.name} setelah bonus (intern): {self.salary}")

    def __init__(self, name, salary, duration):
        super().__init__(name, salary)
        self.duration = duration  # dalam bulan

    # Override method
    def info(self):
        print(f"{self.name}, gaji: {self.salary}, status: intern selama {self.duration} bulan")

class Engineer(Employee):
    def languages(self, langs):
        print(f"{self.name} menguasai bahasa {', '.join(langs)}") # , ".join(langs) akan mengubah list itu jadi string yang rapi dipisahkan koma.

# Buat objek dari kelas Employee
emp1 = Employee("Alice", 7000000)
emp1.info()

# method bonus dari class Employee
emp1.bonus(500000)

# Buat objek dari class Engineer
eng1 = Engineer("Bob", 8000000)
eng1.info()

eng1.languages(["Python", "JavaScript"])
