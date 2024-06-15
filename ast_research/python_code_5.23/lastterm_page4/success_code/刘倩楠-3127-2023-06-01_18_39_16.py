n=eval(input())
ls=[x for x in range(1,n+1,1)]
a=ls[0]
ls.remove(a)
ls.append(a)
print(ls)
