list1=eval(input())
list2=[]
for x1 in list1:
    ini=0
    for x2 in list1:
        if x1==x2:
            ini+=1
    if ini==1:
        list2.append(x1)
list2.sort()
if list2==[]:
    print("False")
else:
    print(','.join(str(x) for x in list2))
