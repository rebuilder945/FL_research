lst=eval(input())
for i in lst:
    sums=0
    sums=sums+i+"+"
print(sums)
avg=sums/len(lst)
for i in avg:
    i=str(i)
    if i.count('.')==1:
        print("%.2f"%i)
    else:
        print(i)
