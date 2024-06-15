n,m,l=eval(input())
n=[n]
for x in range(1,m):
    n+=[n+n*l]
print(n)

