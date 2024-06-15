lst=eval(input())
da=max(lst)
xiao=min(lst)
for i in lst:
    if i==da or i==xiao:
        lst.remove(i)
print(lst)


