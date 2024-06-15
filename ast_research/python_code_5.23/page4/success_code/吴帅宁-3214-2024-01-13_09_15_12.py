ls=eval(input())
count=0
tmp=ls.copy()
for i in range(len(ls)-1):
    if ls[i]==0:
        tmp.remove(ls[i])
        count+=1
count_ls=[0 for x in range(count)]
print(tmp+count_ls)
