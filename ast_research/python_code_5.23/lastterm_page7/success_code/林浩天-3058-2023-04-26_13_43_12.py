string={}
while True:
    s=input()
    if s =="q":
        break
    if s in string:
        string[s]+=1
    else:
        string[s]=1
maxc=0
maxs=""
for s,c in string.items():
    if c >maxc:
        maxc=c
        maxs=s
print(maxs,maxc)

       
