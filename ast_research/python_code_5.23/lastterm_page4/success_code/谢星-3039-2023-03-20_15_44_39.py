lst=eval(input())
a=max(lst)
b=min(lst)
for i in lst:
    if i==a or i==b:
        del lst[i]
print(lst)

