lst=eval(input())
sum0=sum(lst)
min0=min(lst)
for x in range(len(lst)):
    if sum0 in lst:
        lst.remove(sum0)
    else:
        break
for x in range(len(lst)):  
    if min0 in lst:
        lst.remove(min0)
    else:
        break
print(lst)


