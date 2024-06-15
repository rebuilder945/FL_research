n=int(input())
lit=[x for x in range(1,n+1)]
a=lit[0]
lit.pop(0)
lit.append(a)
print(lit)
