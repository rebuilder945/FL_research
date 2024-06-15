lst=eval(input())
lst1=[]
for i in lst[::]:
    if i==2:
        lst1.append(i)
    else:
        for x in range(2,i):
            if i%x==0:
                break
            else:
                lst1.append(i)
                break
print(lst1)

