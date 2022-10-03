import math
x = float(input("Введіть початок діапазону(число a): "))
y = float(input("Введіть кінець діапазону(число b): "))
h = float(input("Введіть крок для діапазону: "))
while x <= y: 
  y = float(math.pow(x,1/3) + math.fabs(math.sin(x)))
  print("x=%.1f y=%.3f"%(x,y))
  x=x+h