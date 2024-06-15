ls=eval(input())
n,m=input().split(",")
n=int(n)
m=int(m)
ls=list(ls)
if n>m or n>=len(ls) or m>=len(ls):
    print("error")
else:    
    for i in range(n,m):
     ls.pop(i)
    print(ls)


