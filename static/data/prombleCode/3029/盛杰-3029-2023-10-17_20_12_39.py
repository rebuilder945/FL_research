name=list(input().split(","))
score=eval(input())
ls=[]
for i in range(len(name)):
    ls1=[name[i],score[i]]
    ls.append(ls1)
print(ls)



