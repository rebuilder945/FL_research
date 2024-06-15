s=input() or "q"
Count={}
Max=0
while(s!="q"):
    Count[s]=Count.get(s,0)+1
    if Count[s]>Max:
        Max=Count[s]
    s = input() or "q"
for k,v in Count.items():
    if(v==Max):
        print(k,v)
