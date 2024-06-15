lst=eval(input())
# lst.remove(max(lst))
# lst.remove(min(lst))
a=max(lst)
# print(a)
b=min(lst)
s=[]
c=[]
for x in lst:
    if x==a or x==b:
        c.append(x)
    else:
        s.append(x)
print(s)






