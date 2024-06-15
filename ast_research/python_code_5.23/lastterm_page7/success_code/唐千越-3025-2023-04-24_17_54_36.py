slist = input.split()
Count = {}
Max = 0
for s in slist:
    Count[s]=Count.get(s,0)+1
    if Count[s]>Max:
        Max=Count[s]
Countlist = list(Count.itrms())
Countlist.sort()
for k,v in Countlist:
    if v == Max:
        print(k,v)
