a=input().split()
n,m=eval(input())
if n>=0 and n<len(a) or n<0 and -n<=len(a):
    b=[]
    c=a[n]
    b.append(c)
    b=b*m
    a.extend(b)
    print(a)
else:
    print("error")
