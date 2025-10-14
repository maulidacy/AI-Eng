def triangle_area(base: float, height: float) -> float:
    """Return area of a tringle given base and height."""
    return 0.5 * base * height

assert abs(triangle_area(10, 2) - 10.0) < 1e-6
print("OK")