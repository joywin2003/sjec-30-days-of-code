# Code by Joywin

# Takes the total number of elements
n = int(input())

# Takes the n number of elements
array = list(map(int, input().split()))

# pops the extra elements from the list
if len(array) > n:
    raise Exception("Too many input")
elif len(array) < n:
    raise Exception("Too less input")
else:
    # Finds the average of the list
    avg = sum(array) / n
    # Makes a list of numbers greater than the average
    g_array = [ele for ele in array if ele > avg]
    print(g_array)






