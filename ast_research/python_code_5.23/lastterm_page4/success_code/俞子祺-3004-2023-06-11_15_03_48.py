ls=eval(input())
ls1=[]
if 2 in ls:
    ls1.append(2)
for i in ls:
    if i>1:
        for h in range(1,i+1):
            if i%h!=0 and i not in ls1:
                ls1.append(i)
print(ls1)
