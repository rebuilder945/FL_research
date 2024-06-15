n=int(input())
a=list(range(1,n+1))
for i in a:
    a.pop(1)
    a.append(1)
    print(a)

