list=eval(input())
list2=[]
list3=[]
for i in list:
    if list.count(i)==1:
        list2.append(i)
        list2.sort()
        s=",".join(str(e) for e in list2)

    else:
        list3.append(i)
if list3==list:
    prnot int("error")
else:
    print(s)

        



