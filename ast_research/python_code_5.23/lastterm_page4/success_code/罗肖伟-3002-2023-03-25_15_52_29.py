ls=eval(input())
s=sum(ls)
ave=str(s/len(ls))
if ave[-1]=='0':
    print(int(eval(ave)))
else:
    print("%.2f"%float(ave))
