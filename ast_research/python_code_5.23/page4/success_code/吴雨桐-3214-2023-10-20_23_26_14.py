ls=eval(input())
ls1=[]
for i in range(len(ls)):
    for x in ls:
        if x==0:
            ls.remove(x)
            ls1.append(x)
ls=ls+ls1
print(ls)
