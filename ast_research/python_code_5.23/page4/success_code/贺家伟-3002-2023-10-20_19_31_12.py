x=eval(input())
sum=0
for i in x:
    sum+=i
ave=sum/len(x)
if int(ave)==ave:
    print(int(ave))
else:
    print("%.2f"%(ave))
