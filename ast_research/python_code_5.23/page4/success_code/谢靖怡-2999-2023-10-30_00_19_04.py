ls=list(input())
a,b=eval(input()).split(",")
ls[a],ls[b]=ls[b],ls[a]
print(ls)
