a=list(input().split(","))
b,c=eval(input())
d=[]
if b>=len(a):
    print("error")
else:
    for i in range(0,c):
        d.append(a[b])
    a=a+d
    for i in range(0,len(a)):
        a[i]=int(a[i])
    print(a)
