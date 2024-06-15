n=input()
for x in n:
    if x.isdigit()==False:
        n=n.replace(x,"*")
list1=n.split("*")
for i in list1[:]:
    if i=="":
        list1.remove(i)
if list1==[]:
    print("No digit")
list=[]
for m in list1:
    if list==[]:
        list.append(m)
    else:
        if len(m)>=len(list[0]):
            list[0]=m
        else:
            continue
print(list[0])
