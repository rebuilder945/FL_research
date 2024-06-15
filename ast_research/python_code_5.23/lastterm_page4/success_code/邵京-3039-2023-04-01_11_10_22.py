prilist=eval(input())
for i in prilist:
     if prilist.count(i)>=2:
        prilist.remove(i)
print(prilist)

