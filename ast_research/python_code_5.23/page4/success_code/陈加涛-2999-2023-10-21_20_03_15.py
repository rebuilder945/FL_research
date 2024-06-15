b=input().split()
b=list(map(eval,b))
n,m=eval(input())
del b[n]
b.insert(m,b[n])
print(b)
