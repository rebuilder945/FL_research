a=eval(input())
sum=0
for i in range(len(a)):
    sum+=a[i]
ave=sum/len(a)
if ave/1==0:
    print("%d"%ave)
else:
    print("%.2f"%ave)
