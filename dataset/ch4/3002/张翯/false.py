list=eval(input())
sum=0
for i in list:
    sum+=i
ava=sum/len(list)
if ava==sum%len(list):
   print("%.2f"%(ava)) 
else:
    print("%d"%(ava))
