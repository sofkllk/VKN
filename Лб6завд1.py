import math
a = float(input("Введіть початок діапазону(число a): "))
b = float(input("Введіть кінець діапазону(число b): "))
h = float(input("Введіть крок для діапазону: "))
x=a
for i in range (100): 
  y = float(math.pow(x,1/3) + math.fabs(math.sin(x)))
  print("%i x=%.1f y=%.3f"%(i,x,y))
  x=x+h