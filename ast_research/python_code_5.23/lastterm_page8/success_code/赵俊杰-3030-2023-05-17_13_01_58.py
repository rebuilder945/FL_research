ls1=input().split(",")
ls2=eval(input().split(","))
ls3=[]
for i in range(0,len(ls1)):
    ls=[ls1[i],ls2[i]]
    ls3.append(ls)
ls3.sort()
print(ls3)
