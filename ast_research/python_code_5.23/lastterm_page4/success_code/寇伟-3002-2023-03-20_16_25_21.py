ls = eval(input())
s = sum(ls)
ave=str(s/len(ls))
if ave[2]=='0':
    print(int(int(ave)))
else:
    print("%.2f"%float(ave))



