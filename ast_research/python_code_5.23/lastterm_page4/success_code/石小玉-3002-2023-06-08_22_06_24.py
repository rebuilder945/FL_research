nums=eval(input())
a=sum(nums)
b=len(nums)
x=a/b
y=a%b
if y==0:
    print("%d"%(x))
else:
    print("%.2f"%(x))
