ls1=eval(input())
ls3=[]
if 1 in ls1:
    ls3.append(1)
if 2 in ls1:
    ls3.append(2)
for x in ls1:
    for i in range(3,x):
        while x%i!=0:
            ls3.append(x)
            break
        break
print(ls3)
