ls=eval(input())
ls1=ls[:]
s=0
for i in range(len(ls1)):
    if ls[i] == 0:
        ls.remove(0)
        s+=1
ls=str(ls)
m=str([0]*s)
print(ls+m)

