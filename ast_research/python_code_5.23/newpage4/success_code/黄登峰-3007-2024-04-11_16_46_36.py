lst=eval(input())
x=input().split(",")
n=min(x)
m=max(x)
if n>=len(lst)-1:
    print("error")
else:
    del lst[n:m]
    print[lst]
