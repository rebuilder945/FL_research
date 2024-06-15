n=eval(input())
k=[ i for i in range(1,n+1)]
m=k[0]
k.pop(0)
k.append(m)
print(k)
