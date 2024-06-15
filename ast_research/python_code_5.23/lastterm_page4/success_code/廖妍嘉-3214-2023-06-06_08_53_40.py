ls=eval(input())
ls2=[]
ls3=[]
for i in ls:
    if i==0:
        ls2.append(i)
    else:
        ls3.append(i)
ls4=ls3+ls2
print(ls4)

