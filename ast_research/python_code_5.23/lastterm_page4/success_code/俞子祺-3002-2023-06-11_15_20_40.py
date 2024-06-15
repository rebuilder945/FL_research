ls=eval(input())
ave=sum(ls)/len(ls)
if ave-int(ave)==0:
    print(int(ave))
elif ave-int(ave)!=0:
    print("%.2f"%ave)
