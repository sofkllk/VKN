import math
Ax = float(input("Введіть значення x для точки А: "))
Ay = float(input("Введіть значення y для точки А: "))
Bx = float(input("Введіть значення x для точки B: "))
By = float(input("Введіть значення y для точки B: "))
Cx = float(input("Введіть значення x для точки С: "))
Cy = float(input("Введіть значення y для точки С: "))

dA = float (math.sqrt(math.pow(Ax,2)) + math.sqrt(math.pow(Ay,2))) 
print("Відстань від початку координат до точки А: ", dA)
dB = float (math.sqrt(math.pow(Bx,2)) + math.sqrt(math.pow(By,2))) 
print("Відстань від початку координат до точки B: ", dB)
dC = float (math.sqrt(math.pow(Cx,2)) + math.sqrt(math.pow(Cy,2)))
print("Відстань від початку координат до точки C: ", dC)

if dA>dB and dA>dC:
     print("Відстань від А до початку координат найбільша")
elif dB>dA and dB>dC: 
    print("Відстань від B до початку координат найбільша")
elif dC>dA and dC>dB: 
    print("Відстань від B до початку координат найбільша")

else: print("Всі точки на однаковій відстані")
input("відповідь.")