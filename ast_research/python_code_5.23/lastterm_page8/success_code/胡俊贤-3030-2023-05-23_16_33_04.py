names=input().split()
scores=input().split()
ls={}
for i in range(len(names)):
    ls[names[i]]=scores[i]
ls=list(ls.items())
print(ls)

