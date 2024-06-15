ls=eval(input())
n=0
m=ls.count(0)
ls1=[0]*len(ls)
for i in ls:
    if i >0 or i<0:
        ls1[n]=i
        n+=1
print(ls1)
