lz=list(input())
ls=lz.split(sep=" ")
a,b=eval(input()).split(",")
ls[a],ls[b]=ls[b],ls[a]
print(ls)
