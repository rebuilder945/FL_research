name=input().split(",")
score=eval(input())
ls1=list(name)
ls2=[]
ls3=[]
for i in range(len(ls1)):
    ls2=[ls1[i],score[i]]
    ls3.append(ls2)
print(ls3)
