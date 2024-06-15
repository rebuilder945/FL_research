lst1=eval(input())
lst2=lst1.copy()
a=max(lst2)
b=min(lst2)
if lst1.count(a)+lst1.count(b)==len(lst1):
    lst1.clear()
elif lst1.count(a)==len(lst1):
    lst1.clear()
elif lst1.count(b)==len(lst1):
    lst1.clear()
else:
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

