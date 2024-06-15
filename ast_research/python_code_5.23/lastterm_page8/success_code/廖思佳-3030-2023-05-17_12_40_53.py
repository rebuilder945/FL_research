names=input().split(",")
scores=input().split(",")
all=[]

for  i  in list(range(len(names))):
    k=[names[i],int(scores[i])]
    all.append(k)
all.sort(key=lambda x:x[1])
print(all)


