a=input().split(",")
a=[int(i) for i in a]
n,m=eval(input())
if n>len(a)-1:
    print("error")
else:
    b=[]
    b.append(a[n])
    b=b*m
    l=a+b
    print(l)





