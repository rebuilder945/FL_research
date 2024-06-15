lst=eval(input())
a=[]
b=max(lst)
c=min(lst)
for i in lst:
    if c<i<b:
        a.append(i)
print(a)
