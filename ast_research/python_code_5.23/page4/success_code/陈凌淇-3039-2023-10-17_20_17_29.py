lst=eval(input())
a=max(lst)
b=min(lst)
lit1=lst.copy()
for x in lst:
    if x==a or x==b:
       lit1.remove(x)
print(lit1)
