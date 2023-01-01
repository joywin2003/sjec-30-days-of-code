# Code by Joywin
from math import sqrt
PI = 3.14

p = int(input())
q = int(input())
r = int(input())
s, t = map(int, input().split())

area_dict = {
    "Circle": PI*p**2,
    "Triangle": round((sqrt(3)/4)*(r**2),2),
    "Square": q**2,
    "Rectangle":s*t

}
# Sorts the dictionary values based on key
ordered_dict = sorted(area_dict, key=lambda x: area_dict[x], reverse=True)

# Loop to print all shapes in descending order
for shapes in ordered_dict:
    print(shapes)
