lst=eval(input())
lst2=lst.copy()
sushu=[]
oushu=[]
for i in lst2:
    if i==2 or i==1:
        sushu.append(i)
    else:
        for x in range(2,i):
            if i%x==0:
                oushu.append(i)
for i in lst2:
    if i in oushu:
        continue
    else:
        sushu.append(i)
print(sushu)
