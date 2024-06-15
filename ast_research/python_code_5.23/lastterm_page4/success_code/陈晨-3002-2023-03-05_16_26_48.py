lst=eval(input())
total=sum(lst)
ilen=len(lst)
pj=total/ilen
if pj-(pj//1)==0:
    print(int(pj))
else:
    print("%.2f"%(pj))
