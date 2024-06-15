ls1=input().split(",")
ls2=input().split(",")
ls4=eval(ls2)
ls3=[]
for i in range(0,len(ls1)):
    ls=[ls1[i],ls4[i]]
    ls3.append(ls)
ls3.sort()
print(ls3)
