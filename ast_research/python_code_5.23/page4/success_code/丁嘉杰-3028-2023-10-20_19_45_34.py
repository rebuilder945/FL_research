ls1=input().split(",")
n=eval(ls1[0])
m=eval(ls1[1])
l=eval(ls1[2])
ls2=[]
for i in range (0,m):
    x=n+i*l
    ls2.append(x)
print(ls2)

