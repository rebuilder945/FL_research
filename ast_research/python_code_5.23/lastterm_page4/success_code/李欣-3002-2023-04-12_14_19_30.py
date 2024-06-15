ls1=eval(input())
e=sum(ls1)/len(ls1)
if e-int(e)==0:
    print(int(e))
else:
    print("%.2f"%e)
