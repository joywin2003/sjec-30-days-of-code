# Code by Joywin

def fbb(x, y: int) -> str:
    for i in range(x, y+1):
        if i % 3 == 0:
            print("Foo")
        elif i % 2 == 0:
            print("Bar")
        else:
            print("Baz")


a, b = map(int, input("Enter the values of a and b:").split())
fbb(a, b)
