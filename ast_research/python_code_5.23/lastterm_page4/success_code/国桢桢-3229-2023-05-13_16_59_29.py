l = eval(input())
l1 = []
for i in l:
    if l.count(i)==1:
        l1.append(i)
l1.sort(reverse =False)
if len(l1)==0:
    print(False)
else:
    str=','.join(str(item)for item in l1)
    print(str)
