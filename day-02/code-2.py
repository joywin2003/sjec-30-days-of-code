# Code by Joywin

def smallest(sides):
    sides.sort()
    print(sides[0])


def largest(sides):
    sides.sort()
    print(sides[2])


def medium(sides):
    sides.sort()
    print(sides[1])


def compute(tlist, num: int):
    for j in range(num):
        if j % 3 == 0:
            smallest(tlist[j])
        elif j % 3 == 1:
            medium(tlist[j])
        else:
            largest(tlist[j])


n = int(input())
triangle_list = []
for i in range(n):
    a, b, c = map(int, input().split())
    triangle_list.append([a, b, c])
compute(triangle_list, n)
