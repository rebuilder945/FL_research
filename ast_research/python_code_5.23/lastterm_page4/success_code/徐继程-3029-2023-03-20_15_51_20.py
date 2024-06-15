ls11=input()
ls1=ls11.split(',')
lsnum=eval(input())
ls=[]
for i in range(3):
    ls0=[ls1[i],lsnum[i]]
    ls.append(ls0)
print(ls)
