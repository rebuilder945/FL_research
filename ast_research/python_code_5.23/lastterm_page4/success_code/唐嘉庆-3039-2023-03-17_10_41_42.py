lst=eval(input())
a=max(lst)
b=min(lst)
lst.remove(a)
lst.remove(b)
if a or b in lst:
    lst.remove(a)
    lst.remove(b)
    print(lst)
else:
    print(lst)

    
