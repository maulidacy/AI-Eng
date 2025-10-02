# Simple calculator with validation
def kalkulator(a_str, b_str, operator):
    try:
        a = float(a_str)
        b = float(b_str)
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
        else:
            return "Operator tidak valid"
    except ValueError:
        return "Input tidak valid"