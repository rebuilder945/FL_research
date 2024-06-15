ls=eval(input())
lst=[]
for i in range(len(ls)):
    if ls.count(ls[i]) == 1:
        lst.append(ls[i])
    lst.sort()
print(lst)
