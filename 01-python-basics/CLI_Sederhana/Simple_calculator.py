# Simple calculator with validation
def kalkulator(a_str, b_str, operator):
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        return "Input harus angka."
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: Pembagian dengan nol tidak dapat dilakukan."
        return a / b
    else:
        return "Operator tidak valid"

# contoh interaksi sederhana
a = input("Masukkan angka pertama: ")
b = input("Masukkan angka kedua: ")
operator = input("Masukkan operator (+, -, *, /): ")
print(f"{a} {operator} {b} = {kalkulator(a, b, operator)}")