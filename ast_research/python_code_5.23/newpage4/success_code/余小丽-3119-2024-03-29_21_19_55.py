lst=eval(input())
for i in lst:
    a=lst.count(i)
    if a>=1:
        lst.remove(i)
print(lst)
