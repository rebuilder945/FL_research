list=eval(input())
li=[]
for i in list:
    if list.count(i)==1:
        li.append(i)
        li.sort()
if li!=[]:
    separator=','
    print(separator.join(str(i) for i in li))
else:
    print("False")



