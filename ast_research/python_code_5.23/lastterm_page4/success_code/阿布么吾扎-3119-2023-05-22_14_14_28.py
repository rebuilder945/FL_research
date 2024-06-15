lst=eval(input())
a=len(lst)
ls=[]
for i in range(a-1,-1,-1):
    if lst[i] not in ls:
        ls.append(lst[i])
ls.reverse()
print(ls)
