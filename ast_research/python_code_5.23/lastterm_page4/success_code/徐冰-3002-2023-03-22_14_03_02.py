nums=eval(input())
a=sum(nums)/len(nums)
if sum(nums)%len(nums)==0:
    print("%d"%(a))
else:
    print("%.2f"%(a))
