lst=eval(input())
for i in lst:
    if i ==0:
        lst.remove(i)
        lst.append(i)
print(lst)




