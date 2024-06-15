a=eval(input())
b,c=eval(input().split(","))
d=[]
if b>=len(a):
    print("error")
else:
    d.append(a[b]*c)
    a=a+d
    print(a)
