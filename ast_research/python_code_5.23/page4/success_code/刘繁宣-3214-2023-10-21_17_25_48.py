ls=eval(input())
ls2=[]
ls3=[]
for i in range(len(ls)):
    if ls[i] != 0:
        ls2.append(ls[i])
    else:
        ls3.append(ls[i])
ls4=ls2+ls3
print(ls4)
