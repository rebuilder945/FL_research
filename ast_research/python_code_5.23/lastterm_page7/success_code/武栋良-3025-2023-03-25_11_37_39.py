lst = input().split()
lst1 = []
for x in lst:
    if x not in lst1:
        lst1.append(x)
lst1.sort()
dit = {}
for x in lst1:
    b = lst.count(x)
    dit[x] = b
lst1 = list(dit.values())
c = max(lst1)
for x in dit:
    if dit[x]==c:
        print(x,c)

    

