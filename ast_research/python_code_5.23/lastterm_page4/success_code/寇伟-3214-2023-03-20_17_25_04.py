ls=eval(input())
ls1=ls[:]
s=0
for i in ls1:
    if i == 0:
        ls.remove(0)
        s+=1

m=[0]*s
print(ls+m)

