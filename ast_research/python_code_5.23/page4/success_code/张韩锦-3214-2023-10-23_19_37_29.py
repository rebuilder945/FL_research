lst=eval(input())
a=len(lst)
lst2=[0]
for i in lst:
    if i == 0:
        lst.remove(i)
b=len(lst)
lst2=lst2*(a-b)
print(lst+lst2)
