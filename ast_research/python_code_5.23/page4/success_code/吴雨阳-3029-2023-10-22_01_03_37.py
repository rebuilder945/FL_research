ls1=input().split(",")
ls2=eval(input())
print(ls1,type(ls1))
print(ls2,type(ls2))
ls3=[]
for i in range(len(ls1)):
    ls3.append([ls1[i],ls2[i]])
print(ls3)
