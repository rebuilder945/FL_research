names=input().split(",")
scores=eval(input())
ls=[]
for x in list(range(len(names))):
    ml=[names[i],scores[i]]
    ls.append(ml)
print(ls)
