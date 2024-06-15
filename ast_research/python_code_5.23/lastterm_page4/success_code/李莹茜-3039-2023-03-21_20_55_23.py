ls=eval(input())
smax=max(ls)
smin=min(ls)
lscopy=ls.copy()
for x in lscopy:
    if x==smax or x==smin:
        ls.remove(x)
print(ls)
