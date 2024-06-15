lst=eval(input())
lst2=lst.copy()
sushu=[]
for i in lst2:
    if i==0:
        lst.remove(i)
    elif i==1:
        lst.remove(i)
    elif i<0:
        lst.remove(i)
    elif i==2:
        sushu.append(i)
    else:
        for n in range(2,i):
            if i%n==0:
                break
        else:
            sushu.append(i)
sushu2=[]
for i in sushu:
    if i not in sushu2:
        sushu2.append(i)
    else:
        pass
print(sushu2)
