# Code by Joywin

# Takes value on m and n
m, n = map(int, input("Enter m and n:").split())

if m * n % 6 == 0 and m != 1 and n != 1:
    print("Yes")
else:
    print("No")
