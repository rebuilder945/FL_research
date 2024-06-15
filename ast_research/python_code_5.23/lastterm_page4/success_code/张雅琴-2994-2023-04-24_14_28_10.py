a=eval(input().split(","))
n,m=eval(input().split(","))
lst1=list(a)
if n>=len(lst1):
    print("error")
else:
    num=int(lst1[n])
    b=[num]*m
    c=lst1+b
    print(c)

