import math
x = float(input("Введіть початок діапазону(число a): "))
y = float(input("Введіть кінець діапазону(число b): "))
h = float(input("Введіть крок для діапазону: "))
spisok=[]
while x <= y: 
  z = float(math.pow(x,1.0/3.0) + math.fabs(math.sin(x)))
  spisok.append(z)
  x=x+h

print(spisok)