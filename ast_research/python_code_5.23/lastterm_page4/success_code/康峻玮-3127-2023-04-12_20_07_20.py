n=eval(input())
ls=[x for x in range(1,n+1)]
y = ls[0]
for x in range(n-1):
    ls[x]=ls[x+1]
ls.pop()
ls.append(y)
print(ls)

