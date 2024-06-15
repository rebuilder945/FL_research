ls1=input().split(",")
ls2=eval(input())
ls3=[]
for i in range(0,len(ls1)):
    a=str(ls1[i])+str(ls2[i])
    ls3.append(a)
print(ls3)
