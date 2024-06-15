lst=eval(input())
x=input().split("，")
n=int(min(x))
m=int(max(x))
if n>=len(lst) and m>=len(lst):
    print("error")
else:
    del list[n:m]
    print[lst]
