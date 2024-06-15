ls=eval(input())
ls1=[]
for i in ls:
    if i==2:
        ls1.append(i)
    elif i>2:
        for h in range(2,i):
            if i%h!=0 and i not in ls1:
                ls1.append(i)
print(ls1)

