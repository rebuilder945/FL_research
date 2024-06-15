str1=input()
str2=input()
if len(str1)==len(str2):
    list1=str1.split()
    list2=str2.split()
    a=0
    for i in str1:
        if list1.count(i)==list2.count(i):
            a+=1
    if a==len(str1):
        print('True')
    else:
        print('False')
else:
    print('False')

