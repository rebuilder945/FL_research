lst=eval(input())
for i in lst:
    if i==0:
        lst.remove(i)
        lst.append(0)
print(lst)
