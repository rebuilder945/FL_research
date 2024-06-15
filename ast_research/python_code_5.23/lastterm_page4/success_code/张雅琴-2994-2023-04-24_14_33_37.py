a=input().split(",")
d=a.strip()
n,m=eval(input())
lst1=list(d)
if n>=len(lst1):
    print("error")
else:
    num=int(lst1[n])
    b=[num]*m
    c=lst1+b
    print(c)

