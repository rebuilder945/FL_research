def xu(ls,score):
    ls1=[]
    for h in range(len(ls)):
        for i in range(len(ls)):
            a=min(score)
            if  ls[i][1]==a  :
                ls1.append(ls[i])
                score.remove(a)
                break
    print(ls1)
name=input().split(',')
score=list(eval(input()))
ls=[]
for x in range(len(name)):
    ls.append([name[x],score[x]])
xu(ls,score)
