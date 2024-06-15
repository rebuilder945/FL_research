ls=eval(input())
ls2=[]
for i in ls:
    if ls.count(i)==1:
        ls2.append(i)
        ls2.sort()
        a=ls2
    else:
        a='False'
print(a)

