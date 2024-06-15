name=input().split(',')
score=input().split(',')
ls=[]
for i in range(len(name)):
    b=[name[i],eval(score[i])]
    ls.append(b)
ls.sort(key=lambda x:x[1],reverse=False)
print(ls)
