# Class = template (cetakan)
# Object = instance dari class
# Method = fungsi/aksi yang ada di dalam class
# Attribute = variabel, data tiap object

# Class Employee (definisi umu -> template)
#------------------------------------------class dengan Atribut & Method Dasar----------------------------------
class Employee:
    


#------------------------------------------CONSTRUCTOR------------------------------------------
class Employee:
    def __init__(self, name, age, salary): # constructor
        self.name = name
        self.age = age
        self.salary = salary

# saat emp1 dibuat, constructor langsung jalan -> atribut name, age, salary terisi
emp1 = Employee("Ayu", 23, 7000000) # constructor dipanggil otomatis

# tanpa constructor, harus diisi secara manual
# emp1 = Employee()
# emp1.name = "Ayu"
# emp1.age = 23
# emp1.salary = 7000000 
