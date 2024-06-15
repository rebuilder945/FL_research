a=list(eval(input()))
n,m=eval(input())
if n<len(a)-1:
    for x in range(m):
        a.append(a[n])
    print(a)
else:
    print("error")
