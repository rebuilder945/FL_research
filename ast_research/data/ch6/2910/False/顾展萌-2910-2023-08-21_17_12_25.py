h = eval(input())
N = eval(input())
m = h
if N == 1:
     print("%.2f"%h)
else:
     for i in range(2,N+1):
          m+=2*(0.5)**(i-2)*h
     print("%.2f"%m)

