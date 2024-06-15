lz=list(input())
ls=lz.split(sep=" ")
a,b=eval(input()).split(",")
c=ls[a]
d=ls[b]
ls[a]=d
ls[b]=c
print(ls)
