al=input().split(",")
bl=list(eval(input()))
ls=[]
for x in range(len(al)):
    ls.append([al[x],bl[x]])
ls.sort(key=x[1])
print(ls)
