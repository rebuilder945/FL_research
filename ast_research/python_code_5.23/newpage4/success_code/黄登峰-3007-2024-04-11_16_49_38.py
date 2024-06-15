a=eval(input())
b=list(map(int,input().split(",")))
n=b[0]
m=b[1]
if m<=len(a)-1 and n<=len(a)-1:
    del a[n:m]
    print(a)
else:
    print("error")
