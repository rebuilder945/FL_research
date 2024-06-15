str1="abcdefghijklmnopqrstuvwxyz"
str2=str1.upper()
lst1=list(str1)
lst2=list(str2)
lst3=[]
lst=list(input())
for i in lst:
    if i.isupper():
        lst3.append(lst2[25-lst2.index(i)])
    elif i.islower():
        lst3.append(lst1[25-lst1.index(i)])
    else:
        lst3.append(i)
print("".join(lst))
print("".join(lst3))
