a=input()
b=eval(input())
a=list(a.split(","))
l2=[]
for i in range(len(b)):
    l1=[]
    l1.append(a[i])
    l1.append(b[i])
    l2.append(l1)
print(l2)


