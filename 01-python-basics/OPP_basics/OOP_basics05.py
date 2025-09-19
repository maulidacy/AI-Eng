#========================================== Inheritance ==========================================
# Inheritance adalah konsep OOP yang memungkinkan sebuah kelas (class) untuk mewarisi atribut dan metode dari kelas lain.
# Ini memungkinkan untuk membuat hierarki kelas dan mempromosikan penggunaan kembali kode (code reusability).
# Kelas yang mewarisi disebut subclass (kelas turunan), sedangkan kelas yang diwarisi disebut superclass (kelas induk).

# Parent class (superclass)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"{self.name}, gaji: {self.salary}")