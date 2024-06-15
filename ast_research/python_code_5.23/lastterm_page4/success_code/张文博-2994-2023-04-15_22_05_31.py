k=eval(input())
a,b=eval(input())
m=[x for x in k]
if a>len(m) or a<-len(m):
    print("error")
else:
    n=m
    for p in range(b):
        n.append(m[a])
    print(n)
