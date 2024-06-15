lst1=eval(input())
lst2=lst1[::-1]
lst3=[]
for i in lst2:
    if i not in lst3:
        lst3.append(i)
lst4=lst3[::-1]
print(lst4)
