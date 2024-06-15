h=eval(input())
N=eval(input())
lst=[]
for i in range(N-1):
    x=(1/2)**(i)*h
    lst.append(x)
print("%.2f"%sum(lst))
