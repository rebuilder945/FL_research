lst=list(eval(input()))
lstcopy=lst.copy()
for i in lst:
    for x in range(len(lst)):
        if lstcopy.count(i)>1:
            lstcopy.remove(i)
print(lstcopy)

