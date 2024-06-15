ch=input()
xx={}
while ch!='q':
    if ch in xx:
        xx[ch]+=1
    else:
        xx.setdefault(ch,1)
    ch=input()
mm=max(xx.values())
for i in xx:
    if xx[i]==mm:
        print("%s %d"%(i,mm))
        break
