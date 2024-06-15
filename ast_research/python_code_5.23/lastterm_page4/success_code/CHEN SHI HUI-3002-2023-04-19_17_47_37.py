l=eval(input())
avg=sum(l)/len(l)
if (avg%1==0):
    print(int(avg))
else:
    print("%.2f"%avg)
