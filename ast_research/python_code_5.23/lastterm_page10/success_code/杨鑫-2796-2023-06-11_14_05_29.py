s0=input()
long=0
lmax=0
jieguo=[]
for x in range(len(s0)):
    if s0[x].isdigit():
        long=1
        for y in range(x+1,len(s0)):
            if s0[y].isdigit():
                long+=1
                continue
            else:
                break
        if long>=lmax:
            lmax=long
            jieguo.append(s0[x:(x+long)])
if len(jieguo)==0:
    print("No digits")
else:
    print(jieguo[-1])

    

