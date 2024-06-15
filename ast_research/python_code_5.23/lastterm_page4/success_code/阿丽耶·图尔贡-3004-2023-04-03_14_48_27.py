lst=eval(input())
if 1 in lst:
    lst.remove(1)
else:
    pass
if 0 in lst:
    lst.remove(0)
else:
    pass
for x in lst:
    k=lst.index(x)
    if x==2:
        pass
    else:
      for s in range(2,x):
        if x%s!=0:
            pass
        else:
            lst[k]="k"
while "k" in lst:
 lst.remowe("k")
print(lst)
