a=list(eval(input()))
n,m=eval(input())
for i in range(len(a)):
    if n>i:
        print("error")
    else:
        b=[a[n]]*m
        c=a+b
        print(c)
        
