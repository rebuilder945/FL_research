list1=list(input())
list2=[]
list3=[]
str1=''
for i in list1:
    a=(int(i)+5)%10
    list2.append(a)
for x in reversed(list2):
    list3.append(x)
for a in list3:
    str1=str1+str(a)
print(str1)

