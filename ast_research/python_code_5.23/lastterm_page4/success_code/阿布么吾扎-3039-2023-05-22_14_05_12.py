lst=eval(input())
a=max(lst)
b=min(lst)
ls=[]
for x in lst:
    if x>b and x<a:
        ls.append(x)
print(ls)

