ls=eval(input())
ls1=[]
for i in ls:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        ls1.append(i)
print(ls1)
