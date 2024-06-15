lst=eval(input())
for i in lst:
    if i==0 or i==1:
        lst.remove(i)
    elif i==2:
        pass
    else:
        for x in range(2, i-1):
            if i%x==0:
                lst.remove(i)
                break
print(lst)
