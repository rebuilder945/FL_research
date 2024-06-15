lst=eval(input())
sum0=sum(lst)
min0=min(lst)
for x in range(len(lst)):
    if sum0 in lst:
        lst.pop(sum0)
    elif min0 in lst:
        lst.pop(min0)
    else:
        break


