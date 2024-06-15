ls1=input().split(',')#tom,jack,jone,mike

ls2=eval(input())#[88,89,34,90]
ls3=[]
l=int(len(ls1))
#print(len(ls1))

for i in range(l):
    a=[]
    a.append(ls1[i])
    a.append(ls2[i])
    ls3.append(a)

print(ls3)


