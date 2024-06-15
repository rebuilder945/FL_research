name=input().split(',')
score=eval(input())
n1=list(name)
n=len(n1)
ls1=[]
ls2=[]
for i in range(n):
    ls1=[n1[i],score[i]]
    ls2.append(ls1)
print(ls2)
