n=int(input())
lit=[]
for i in range(1,n+1):
    lit.append(i)
a=lit[0]
lit.remove(a)
lit.append(a)
print(lit)

