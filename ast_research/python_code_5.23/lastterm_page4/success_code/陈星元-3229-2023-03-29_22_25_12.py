list=eval(input())
list2=[]
i=0
num=""
for x in list:
    if list.count(x)==1:
        list2.append(x)
    else:
        i+=1
list2.sort()
if i==len(list):
    print("False")
else:
    for x in list2:
        num=num+str(x)+","
        num2=num[0:-1:1]
    print(num2)

