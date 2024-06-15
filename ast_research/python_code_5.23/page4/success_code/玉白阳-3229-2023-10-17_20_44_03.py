list1 = eval(input())
list2 = []
for i in range(len(list1)):
    if list1.count(list1[i])==1:
        list2.append(list1[i])
    else:
        pass
list2.sort()
if list2==[]:
    print("False")
else:
    n1=[str(x) for x in list2]
    n2=",".join(n1)
    print(n2)


