date=eval(input())
n=sum(date)/len(date)
if n%1==0:
    print(int(n))
else:
    print("%.2f" %(n))

