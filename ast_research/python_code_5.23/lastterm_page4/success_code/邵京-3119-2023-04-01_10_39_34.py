prilist=eval(input())
for i in prilist:
    while prilist.count(i)>=2:
        prilist.remove(i)
print(prilist)

