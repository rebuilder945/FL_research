ls1=input.split(",")
ls2=eval(input())
ls3=[]
for i in range(len(ls1)):
    x=[]
    x.append(ls1(i))
    x.append(ls2(i))
    ls3.append(x)
print(ls3)

