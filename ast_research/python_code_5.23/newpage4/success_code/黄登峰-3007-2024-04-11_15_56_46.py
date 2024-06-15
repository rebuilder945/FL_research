lst=eval(input())
x=list(input())
n=int(min(x))
m=int(max(x))
if n>=len(lst)+1:
    print("error")
else:
    del list[n:m]
    print[lst]
