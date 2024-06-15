names=input().split()
scores=input().split()
scores=[int(scores[i]) for i in scores]
ls=[]
for x in range(len(names)):
    ls.append([names[x],scores[x]])
ls.sort(key=lambda x:x[1])
print(ls)
