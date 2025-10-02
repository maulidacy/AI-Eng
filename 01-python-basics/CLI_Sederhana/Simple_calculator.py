# Simple calculator with validation
def kalkulator(a_str, b_str, operator):
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
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
        return "Input tidak valid"