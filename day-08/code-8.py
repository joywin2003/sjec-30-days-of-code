# Code by Joywin

m = int(input())
n = int(input())

# list of prime numbers between m and n
prime = [i for i in range(m, n) if all(i % j != 0 for j in range(2, i))]

# looping and printing the result
for i in range(len(prime) - 1):
    print(f"{prime[i]}-{prime[i + 1]}={prime[i + 1]-prime[i]-1}")
