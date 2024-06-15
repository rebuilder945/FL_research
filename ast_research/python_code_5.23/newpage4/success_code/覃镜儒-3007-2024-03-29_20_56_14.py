i=eval(input())
n,m=eval(input())
if n<len(i)and n<=m:
    del i[n:m]
else:
    print("error")
