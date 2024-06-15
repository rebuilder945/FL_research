ls=list(input())
a,b=eval(input())
c=ls[a]
ls[a]=ls[b]
ls[b]=c
print(ls)
