lst=eval(input())
slst=lst.copy()
for i in lst:
    a=lst.count(i)
    if a>1:
        slst.remove(i)
print(slst)
