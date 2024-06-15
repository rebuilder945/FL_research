str1=input()
str2=input()
list1=[]
list2=[]
for i in str1:
    list1.append(i)
for i in str2:
    list2.append(i)
list1.sort()
list2.sort()
if list1==list2:
    print('True')
else:
    print('False') 


