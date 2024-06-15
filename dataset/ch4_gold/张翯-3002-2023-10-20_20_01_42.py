list=eval(input())
sum=0
for i in list:
    sum+=i
a=sum/len(list)
b=sum//len(list)
if a==b:
    print("%d"%(a))
else:
    print("%.2f"%(a))

