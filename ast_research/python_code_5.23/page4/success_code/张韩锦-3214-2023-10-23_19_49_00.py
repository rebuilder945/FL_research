lst=eval(input())
a=len(lst)
lst2=[0]
lst3=lst.copy()
for i in lst:
    if i == 0:
        lst3.remove(i)
b=len(lst3)
lst2=lst2*(a-b)
print(lst3+lst2)
