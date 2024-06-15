ls=eval(input())
ls1=[]
for i in ls:
    if i == 2:
        ls1.append(i)
        ls1.remove(i)
    else:
        for x in range(2,i):
            if i%x==0:
                ls1.append(i)
                ls.remove(i)
print(ls)



