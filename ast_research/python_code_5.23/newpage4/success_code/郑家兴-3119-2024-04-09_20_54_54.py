lst=eval(input())
for i in lst:
    if lst.count(i) >= 2:
        lst.remove(i)
print(lst)
