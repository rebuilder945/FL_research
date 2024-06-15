lst=eval(input())
for x in lst:
    for i in x:
        sums=x.count(i)
        print(i,sums)
