lst = eval(input())
count = {}
for s in lst:
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
for c in sorted(count.keys()):
    print("%s,%d" % (c,count[c]))
