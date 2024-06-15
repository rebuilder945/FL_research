h=eval(input())
N=eval(input())
m=h
a=h
for i in range(2,N+1):
    a=a*0.5
    m=m+a*2
print("%.2f"%m)
