lst=eval(input())
da=max(lst)
xiao=min(lst)
lstcopy=lst.copy()
for i in lst:
    if i==da or i==xiao:
        lstcopy.remove(i)
print(lstcopy)
