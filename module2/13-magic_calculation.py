def magic_calculation(a, b, c):
    """Return c if a < b, a+b if c > b, otherwise a*b-c."""
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
