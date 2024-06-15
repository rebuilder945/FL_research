lst=eval(input())
sums=0
for x in lst:
    for i in x:
        sums+=x.count(i)
    print(i,sums)
