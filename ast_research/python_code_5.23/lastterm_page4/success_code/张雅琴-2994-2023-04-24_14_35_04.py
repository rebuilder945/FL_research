a=eval(input())
n,m=eval(input())
lst1=list(a)
if n>=len(lst1):
    print("error")
else:
    num=int(lst1[n])
    b=[num]*m
    c=lst1+b
    print(c)

