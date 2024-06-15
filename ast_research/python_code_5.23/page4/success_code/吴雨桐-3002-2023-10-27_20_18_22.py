ls=eval(input())
ave=sum(ls)/len(ls)
if ave-int(ave)==0:
    print(int(ave))
else:
    print("%.2f"%(ave))
