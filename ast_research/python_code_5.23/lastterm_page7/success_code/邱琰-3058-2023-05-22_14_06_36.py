s=input()
Count={}
Max=0
while(s!="q"):
    Count[s]=Count.get(s,0)+1
    if Count[s]>Max:
        Max=Count[s]
for k,v in Count.item():
    if v==Max:
        print(k,v)
