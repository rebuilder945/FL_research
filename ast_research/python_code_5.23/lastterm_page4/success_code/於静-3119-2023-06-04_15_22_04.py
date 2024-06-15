lst=eval(input())
for i in lst:
    if lst.count(i)>1:
            lst.remove(i)
print(lst)

