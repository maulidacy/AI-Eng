def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak dapat dilakukan."
    return a / b

if __name__ == "__main__":
    while True:
        op = input("Pilih operasi [+, -, *, /] atau 'q' untuk keluar: ").strip()
        if op == 'q':