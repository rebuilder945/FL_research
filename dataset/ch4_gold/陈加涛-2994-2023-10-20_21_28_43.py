a=[eval(input())]
n,m=eval(input())
if n in range(0,len(a)+1):
    b=[a[n]]*m
    a.append(b)
elif n in range(-1,-len(a)):
    b=[a[n]]*m
    a.append(b)
else:
    print("error")
