lst=input()[1:-1].split(",")
lst=[eval(i) for i in lst]
for x in lst:
    sum=sum+x
a=sum/len
if a%1==0:
    print(a)
else:
    print("%.2f"%(a))
