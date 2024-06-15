zimu=str(input())
liebiao=list(zimu)
jihe=set(liebiao)
lst=list(jihe)
for x in range(len(lst)):
    if '\'' in lst:
        lst.remove('\'')
lst.sort()
for x in lst:
    d=liebiao.count(x)
    print(x,',',d)

