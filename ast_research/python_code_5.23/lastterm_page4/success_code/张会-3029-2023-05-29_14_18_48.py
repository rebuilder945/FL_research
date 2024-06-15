name=input().split(',')
score=eval(input())
ls=[]
for i in range(len(name)):
    a=[name[i],score[i]]
    ls.append(a)
print(ls)
