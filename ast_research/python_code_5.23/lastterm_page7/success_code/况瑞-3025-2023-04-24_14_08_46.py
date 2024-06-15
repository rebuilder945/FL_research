s=input() or "None"
Count={}
Max=0
while(s !="None"):
    Count[s]=Count.get(s,0)+1
    if Count[s]>Max:
        Max=Count[s]
    s = input() or "None"
for k,v in Count.items():
    if(v==Max):
        print(k)
