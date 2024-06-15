n=eval(input())
lit=[]
for x in range(1,n+1):
    lit.append(x)
lit.append(lit[0])
lit.remove(lit[0])
print(lit)







