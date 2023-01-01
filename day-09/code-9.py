# Code by joywin

n = int(input())

# Print the top traingle
for i in range(n):
    print(" " * (n - i) + "# " * (i + 1))

# Prints the bottom traingle
for j in reversed(range(n-1)):
    print(" " * (n - j) + "# " * (j + 1))
