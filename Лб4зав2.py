import math
a=float(input("введіть змінну a:")),
b=float(input("введіть змінну b:")),
h=float(input("введіть змінну h:")),
x=float(input("введіть змінну x:")),
y=float(input("введіть змінну y:")),
V=(a*b*h*math.cos(x)/3)+(math.log1p(y))
print(V)