count={}
while True:
    s=input()
    if s=="q":
        break
    count[s]=count.get(s,0)+1
valueMax=max(count.values())
for k,v in count.items():
    if v==valueMax:
        print(k,v)
