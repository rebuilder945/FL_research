lst=eval(input())
a=max(lst)
b=min(lst)
list1=lst.copy()
for x in lst:
    if x==max or x==min:
       list1.remove(x)
print(lst)
