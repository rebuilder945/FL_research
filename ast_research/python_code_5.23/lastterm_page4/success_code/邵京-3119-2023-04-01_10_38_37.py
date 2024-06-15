prilist=eval(input())
for i in prilist:
    while prilist.count(i)>1:
        prilist.remove(i)
print(prilist)

