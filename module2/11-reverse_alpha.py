offset = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print(chr(i - offset), end='')
    offset = 0 if offset == 32 else 32
print()
