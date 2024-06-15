a=input().split(",")
n,m=eval(input())
if abs(n)>len(a):
    print("error")
elif abs(n)==len(a) and n>0:
    print("error")
else:
    b=list(a[n])
    c=a+b*m
    b=list(map(int,c))
    print(b)
