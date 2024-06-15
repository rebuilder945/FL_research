val=eval(input())
val.reverse()
lst=[]
for x in val:
    if x not in lst:
        lst.append(x)
lst.reverse()
print(lst)
