ls1=eval(input())
ls2=eval(input())
ls3=[]
for i in range(len(ls1)):
    ls4=[]
    ls4.append(ls1[i])
    ls4.append(ls2[i])
    ls3.append(ls4)
print(ls3)
ls3=[[ls1[i],ls2[i]] for i in range(len(ls1))]
