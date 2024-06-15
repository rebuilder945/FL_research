lst=eval(input())
for i in lst:
    if i ==2 or i==1:
        pass
    if i !=2 and i != 1:
        for m in range(2,i):
            if i % m==0:
                lst.remove(i)
                break
print(lst)




