lst=eval(input())
x=list(map(int,input().split(",")))
n=x[0]
m=x[1]
if n<=len(lst)-1 and m<=len(lst)-1:
    del lst[n:m]
    print[lst]
else:
    print("error")
