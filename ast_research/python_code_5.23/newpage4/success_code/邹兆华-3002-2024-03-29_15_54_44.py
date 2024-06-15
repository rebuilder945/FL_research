s=eval(input())
a=sum(s)/len(s)
if sum(s)%len(s)==0:
   print("%d,"%a)
else:
   print("%.2f,"%a)
