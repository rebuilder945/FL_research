from re import M


n=eval(input())
lst=[]
n=2
m=1
for i in range(1,n+1):
    x=n/m
    n,m=n+m,n
print("%.4f"%sum(lst))


    
