lst1=eval(input())
lst2=lst1.copy()
a=max(lst2)
b=min(lst2)
while True:
    if max(lst1)<a:
        break
    else:
        lst1.remove(a)
while True:
    if min(lst1)>b:
        break
    else:
        lst1.remove(b)
        
print(lst1)

