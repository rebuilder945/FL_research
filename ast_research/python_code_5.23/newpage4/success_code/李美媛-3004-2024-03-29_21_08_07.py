lst=eval(input())
lst1=lst[:]
for i in lst1:
    if i==0 or i==1:
        lst.remove(i)
    else:
        for j in range(2,i):
            if i%j==0:
                break
print(lst)


