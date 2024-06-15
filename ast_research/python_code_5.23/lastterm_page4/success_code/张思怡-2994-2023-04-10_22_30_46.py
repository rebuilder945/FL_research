a=eval(input())
n,m=eval(input())
a=list(a)
# print(a)
if (0-len(a))<=n<len(a):
    b =[a[n]]*m
    print(a+b)
else:
    print("error")
