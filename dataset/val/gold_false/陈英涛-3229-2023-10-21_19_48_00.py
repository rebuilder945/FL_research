l1 = eval(input())
l2 = []
for i in l1:
    if l1.count(i) == 1:
        l2.append(i)
if len(l2) > 0:
    l2.sort()
    s = ",".join(str(e) for e in l2)
    print(s)
else:
    print("false")


     
    

