def add(a: int, b: int) -> int:
    return a + b

a = int(input("First number: ").strip())
b = int(input("Second number: ").strip())

total = add(a, b)
print(f"Sum is {total}")