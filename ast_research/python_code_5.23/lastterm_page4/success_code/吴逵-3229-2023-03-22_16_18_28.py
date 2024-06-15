from collections import Counter

lst = eval(input())
counter = Counter(lst)
res = [x for x in lst if counter[x] == 1]
if not res:
    print(False)
else:
    res.sort()
    print(*res, sep=',')

