a=list(input())
n,m=eval(input())
if abs(n)>len(a):
    print("error")
elif abs(n)==len(a) and n>0:
    print("error")
else:
    b=a.pop(n)
    c=a+b*m
    print(c)
