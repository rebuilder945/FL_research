ls1=eval(input())
e=sum(ls1)/len(ls1)
"{:.2f}".format(e)
x=int(e*100)
if x[-1:-3]==0:
    print(e)
else:
    print("%.2f"%e)
