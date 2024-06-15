ls1=eval(input())
ls2=[]
ls3=[]
for i in ls1:
    if i==2:
        ls2.append(i)
    elif i>2:
        for j in(2,i):
            if i%j==0:
                ls3.append(i)
            else:
                ls2.append(i)
print(ls2)

