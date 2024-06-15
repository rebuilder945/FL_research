a=list(eval(input()))
n,m=eval(input())
if n-1 <= len(a):
    ls1=[a[n]]*m
    ls2=a+ls1
    print(ls2)
else:
    print("error")
