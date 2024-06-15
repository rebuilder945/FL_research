ls1=input().split(",")
ls2=eval(input())
ls1=list(ls1)
ls4=[]
for i in range(len(ls1)):
    ls3=[ls1[i],ls2[i]]
    ls4.append(ls3)
print(ls4)
