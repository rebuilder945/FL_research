h=eval(input())
N=eval(input())
if N==1:
    print("%.2f"%h)
else:
    lst=[h]
    for i in range(2,N+1):
        x=(1/2)**(i-2)*h
        lst.append(x)
    print("%.2f"%sum(lst))
