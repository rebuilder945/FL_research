names=input().split(",")
scores=eval(input())
ls=[]
for x in list(range(len(names))):
    ml=[names[x],scores[x]]
    ls.append(ml)
print(ls)
