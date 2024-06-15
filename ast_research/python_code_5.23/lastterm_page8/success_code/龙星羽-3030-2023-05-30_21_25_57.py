def xu(ls):
    ls1=[]
    for h in range(len(name)):
        for i in range(len(name)):
            if ls[i,1]==min(score):
                ls1.append(ls[i])
                del ls[i]
    print(ls1)
name=input().split(',')
score=input().split(',')
ls=[]
for x in range(len(name)):
    ls.append([name[x],score[x]])
xu(ls)
