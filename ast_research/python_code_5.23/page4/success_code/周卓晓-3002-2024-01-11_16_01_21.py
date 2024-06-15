ls=eval(input())
ave=sum(ls)/len(ls)
a=str(ave)
if a[-1]=="0":
    print(int(ave))
else:
    print("%.2f"%ave)



