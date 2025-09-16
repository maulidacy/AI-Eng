class main:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self._salary = salary   # protected (pakai underscore)

    def info(self):
        print("\n==== Informasi Karyawan ====")
        print(f"Nama: {self.name}")
        print(f"Umur: {self.age}")
        print(f"Gaji: {self._salary}")
        print("============================")
        
    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
            print(f"Gaji {self.name} diperbarui menjadi {self._salary}")
        else:
            print("❌ Gaji tidak boleh negatif!")