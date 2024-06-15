lst=eval(input())
for i in lst:
    if i==0:
        lst.append(int(0))
        lst.remove(0)
print(lst)
