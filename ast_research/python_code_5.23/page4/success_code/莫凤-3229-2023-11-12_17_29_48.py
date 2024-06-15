a=eval(input())
list1=[]
for x in a:
    if a.count(x)==1:
        list1.append(x)
if len(list1)>0:
    list1.sort()
    print(",".jion(list1))
else:
    print("False")
