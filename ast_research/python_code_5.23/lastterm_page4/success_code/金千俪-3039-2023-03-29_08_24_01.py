lst=eval(input())
lstmax=max(lst)
lstmin=min(lst)
for x in lst[:]:
    if x == lstmax or x == lstmin:
        lst.remove(x)
print(lst)

#先找最大值再for
    




