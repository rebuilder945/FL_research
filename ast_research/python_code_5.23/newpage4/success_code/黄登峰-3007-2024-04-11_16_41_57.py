lst=input()
x=list(map(int,input().split(",")))
n=x[0]
m=x[1]
if n<=len(lst):
    del list[n:m]
    print[lst]
else:
    print("error")
