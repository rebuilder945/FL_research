lst=eval(input())
for x in lst:
    if lst.count(x)>1:
        lst.remove(x)
print(lst)

