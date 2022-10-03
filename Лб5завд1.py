import math
x=float(input("Введіть змінну х:"))
def f1(x1):
    rez=math.log10(math.fabs(x+1))+2.9*math.pow(math.e,0.1*x)
    return(rez)
def f2(x2):
    rez=math.sqrt(math.fabs(x))+math.pow(x,1/3)-math.sin(x)
    return(rez)
def f3(x3):
    rez=4*x+math.pow(math.e,x)-4*math.sqrt(math.fabs(x))
    return(rez)
y=0.0
if x>1:
    y=f1(x)
elif x>-1.1 and x<=1:
    y=f2(x)
elif x<=-1.1: 
    y=f3(x)
print(y)
input("відповідь.")
      


