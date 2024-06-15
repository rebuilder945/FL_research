l = eval(input())
l1 = []
for i in l:
    if l.count(i)==1:
        l1.append(i)
l1.sort(reverse =True)
if len(l1)==0:
    print(False)
else:
    print(l1)
