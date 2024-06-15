ls = eval(input())
s = sum(ls)
ave=s/len(ls)
ave=str(ave)
if ave[3]!=0:
    print("%.2f"%ave)
else:
    print(s)
    
