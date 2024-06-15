str1=input()
str2=input()
list1=str1.split()
list2=str2.split()
list1=list1.sort()
list2=list2.sort()
if list1==list2:
    print('True')
else:
    print('False')
