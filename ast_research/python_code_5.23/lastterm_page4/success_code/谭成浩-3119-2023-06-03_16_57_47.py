lst=eval(input())
ls=[]
for i in range(len(lst)):
    if lst[i:].count(lst[i])>1:
        continue
    else:
        ls.append(lst[i])
print(ls)
