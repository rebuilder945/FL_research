def getright(l):
    ls=iter(l)
    count=0
    while True:
        try:
            if next(ls).isdigit():
                    count+=1
            else:
                break
        except StopIteration:
            break
    return count
x=input()
maxx=0
for i in range(len(x)) :
    if x[i].isdigit():
        lt=i
        temp=getright(x[i:])
        rt=lt+temp-1
        if temp>=maxx:
            l,r=lt,rt
if maxx==0:
    print("No digits")
else:
    print(x[l,r+1])
