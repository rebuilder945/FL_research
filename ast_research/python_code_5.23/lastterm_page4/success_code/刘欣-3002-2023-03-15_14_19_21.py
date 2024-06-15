ls=eval(input())
ave=sum(ls)/len(ls)
if ave==int(ave):
    ave=int(ave)
    print(ave)
else:
    print("%.2f"%ave)
