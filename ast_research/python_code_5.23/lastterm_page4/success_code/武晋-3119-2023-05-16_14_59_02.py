lst=eval(input())
for i in lst.copy():
    while i.count>1:
        lst.remove(i)
print(lst)


