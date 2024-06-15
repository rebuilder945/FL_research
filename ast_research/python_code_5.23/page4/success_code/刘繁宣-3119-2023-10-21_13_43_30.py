ls=eval(input())
ls2=ls[::-1]
ls3=[]
for i in range(len(ls)):
    if not ls2[i] in ls3:
        ls3.append(ls2[i])
ls4=ls3[::-1]
print(ls4)
