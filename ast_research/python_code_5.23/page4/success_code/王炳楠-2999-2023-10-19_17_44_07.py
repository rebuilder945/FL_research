a=input()
l=a.split(" ")
l1=l.copy()
l3=l.copy()
b=input()
l2=b.split(" ")
n=eval(l2[0])
m=eval(l2[1])
dl1=l.pop(n)
dl2=l1.pop(m)
l3[n]=dl2
l3[m]=dl1
print(l3)
