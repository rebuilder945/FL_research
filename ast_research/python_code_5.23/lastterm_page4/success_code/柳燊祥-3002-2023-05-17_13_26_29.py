nums=eval(input())
n=sum(nums)/len(nums)
m=sum(nums)%len(nums)
if m==0:
    print(int(n))
else:
    print("%.2f"%(n))
