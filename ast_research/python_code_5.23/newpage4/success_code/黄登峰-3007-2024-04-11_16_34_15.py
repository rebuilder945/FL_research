lst=eval(input())
x=list(input())
n=eval(min(x))
m=eval(max(x))
if n>=len(lst) and m>=len(lst):
    print("error")
else:
    del list[n:m]
    print[lst]
