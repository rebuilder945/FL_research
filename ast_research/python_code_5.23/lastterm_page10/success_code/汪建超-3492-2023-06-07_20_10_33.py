list1=[]
for i in a:
    temp=a.count(i)
    if temp==1:
        list1.append(i)
if len(list1)==0:
    print("None")
else:
    print(list1[0])

