a=input().split(",")
b=eval(input())
ls1=list(a)
ls2=()
ls3=[]
for i in range(len(ls1)):
    ls2=(ls1[i],b[i])
    ls3.append(list(ls2))
print(ls3)






