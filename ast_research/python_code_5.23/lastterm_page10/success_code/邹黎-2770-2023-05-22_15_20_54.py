
a=input()
b=input()
lsta=[]
lstb=[]
for x in a:
    lsta.append([a.count(x),x])
for x in b:
    lstb.append([b.count(x),x])
def yiyang(lst1,lst2):
    for x in lst1:
        if x not in lst2:
            return 1
    for x in lst2:
        if x not in lst1:
            return 1
if yiyang(lsta,lstb):
    print("True")
else:
    print("False")




