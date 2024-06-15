l=eval(input())
n,m=eval(input())
a=[]
l1=l.split()
if n<=len(l1):
    a.append(l1[n])
    b=l1+a*m
    print(b)
else:
    print("error")
