n = str(input())
ls=n.split(' ')
print(ls)
numlst=[ls.count(x) for x in ls]
quchong=sorted(list(set(ls)))
for i in quchong :
    if ls.count(i)==max(numlst):
        print("{} {}".format(i,ls.count(i)))

