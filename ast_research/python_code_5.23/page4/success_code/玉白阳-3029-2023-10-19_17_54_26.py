ls1=list(input())
ls2=input()
ls3=[]
for i in range(len(ls1)-1):
    x=ls1[i-1]
    y=ls2[i-1]
    ls4=[[x,y]]
    ls3.append(ls4,)
if i==range(len(ls1)):
    x=ls1[i-1]
    y=ls2[i-1]
    ls4=[[x,y]]
    ls3.append(ls4)
print(ls3)
