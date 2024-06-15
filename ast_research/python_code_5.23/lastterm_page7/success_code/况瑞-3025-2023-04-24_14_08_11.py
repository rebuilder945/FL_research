s=input() or "none"
Count={}
Max=0
while(s !="none"):
    Count[s]=Count.get(s,0)+1
    if Count[s]>Max:
        Max=Count[s]
    s = input() or "none"
for k,v in Count.items():
    if(v==Max):
        print(k)
