str=input().split()
strlst=",".join(i for i in str)
counter={}
for i in strlst:
    if strlst.count(i)!=1:
        continue
    else:
        counter[i]=1
if counter=={}:
    print("None")
else:
    counterlist=[]
    for k,v in counter.items():
        counterlist.append([k,v])
    print(counterlist[0][0])
