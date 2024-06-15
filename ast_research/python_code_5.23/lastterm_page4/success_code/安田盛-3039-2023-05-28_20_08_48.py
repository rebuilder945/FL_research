lst=eval(input())
a,b=max(lst),min(lst)
while a in lst:
    lst.remove(a)
while b in lst:
    lst.remove(b)
print(lst)


    





