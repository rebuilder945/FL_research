from re import X


lst=eval(input())
lst1=lst.copy()
for i in lst1:
    if i==0:
        lst.remove(x)
        lst.append(x)
print(lst)
