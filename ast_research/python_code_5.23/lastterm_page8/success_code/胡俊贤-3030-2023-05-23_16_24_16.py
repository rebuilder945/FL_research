names=input().split()
scores=input().split()
ls=[]
for i in range(len(names)):
    s=[]
    s.append(names[i])
    s.append(scores[i])
    ls.append(s)
print(ls)
