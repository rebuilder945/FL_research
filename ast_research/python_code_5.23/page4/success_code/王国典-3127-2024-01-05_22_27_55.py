n=eval(input())
ls=[x for x in range(1,n+1)]
a=ls[0]
del ls[0]
ls.append(a)
print(ls)


