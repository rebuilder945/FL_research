h = eval(input())
N = eval(input())
m = h
if N == 1:
     print("%.2f"%h)
else:
     for i in range(1,N):
          m+=2*(0.5)**(i)*h
     print("%.2f"%m)

