list1=[]
list1.append(int(input()))
while list1[len(list1)-1]!=0:
    num1=input()
    list1.append(num1)
    if num1 =='#':
        break
del list1[-1]
list2=[]
for i in list1:
    list2.append(int(i))
a=len(list2)
b=sum(list2)
print(str(a)+" "+str(b))
