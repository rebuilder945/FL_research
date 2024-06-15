ls=eval(input())
ave=sum(ls)/len(ls)
if ave==int(ave):
    print(ls)
else:
    print("%.2f"%ave)
