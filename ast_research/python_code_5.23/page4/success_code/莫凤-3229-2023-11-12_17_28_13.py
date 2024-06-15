a=eval(input())
list1=[]
for x in a:
    if a.count(x)==1:
        list1.append(x)
if len(list1)>1:
    list1.sort()
    for x in list1:
        print(x)
else:
    print("False")
