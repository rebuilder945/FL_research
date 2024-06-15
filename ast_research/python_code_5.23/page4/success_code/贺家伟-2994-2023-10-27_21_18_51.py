a=list(input().split(","))
b,c=eval(input())
d=[]
if b>=len(a):
    print("error")
else:
    d.append(a[b]*c)
    a=a+d
    print(a)
