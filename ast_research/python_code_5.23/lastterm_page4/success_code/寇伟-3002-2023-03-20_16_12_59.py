ls = eval(input())
s = sum(ls)
ave=s/len(ls)
ave=float(ave)
ave=str(ave)
if ave[2]==0:
    print(int(ave))
else:
    print(".2f"%float(ave))

