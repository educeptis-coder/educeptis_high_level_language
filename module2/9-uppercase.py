def uppercase(str):
    """Print a string in uppercase using ASCII arithmetic."""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()
