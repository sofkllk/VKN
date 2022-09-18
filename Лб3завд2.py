import sys
A=int(sys.argv[1])
B=int(sys.argv[2]) 
C=int(sys.argv[3])
k=int(sys.argv[4])
a2 = A*k
b2= B*k
h2= C*k
v=a2*b2*h2
s = 2*a2*b2 + 2*h2*b2 + 2*h2*a2
print(f"{v} - об'єм паралелепіпеда")
print(f"{s} - площа паралелепіпеда")