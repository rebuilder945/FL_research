a=list(eval(input()))


n,m=eval(input())
b=[]
if n in range(0,len(a)+1):
    b.append(a[n])
    b=b*m
    a.extend(b)
    print(a)
else:
    print("error")
