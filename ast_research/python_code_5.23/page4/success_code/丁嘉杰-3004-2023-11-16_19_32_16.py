ls1=eval(input())
ls2=[]
m=1
for i in ls1:
    if i ==2:
        ls2.append(i)
    elif i>2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            ls2.append(i)
print(ls2)
