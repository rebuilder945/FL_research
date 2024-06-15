ls=eval(input())
ave=sum(ls)/len(ls)
if (sum(ls)%len(ls))==0:
    print("%d"%(ave))
else:
    print("%02f"%(ave))
