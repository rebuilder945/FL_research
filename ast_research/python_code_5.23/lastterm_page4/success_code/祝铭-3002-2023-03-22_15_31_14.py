nums = eval(input())
sum = 0
for i in (nums):
    sum+=i
avg = sum/(len(nums))
if avg%1==0:
    print("%d"%(avg))
else:
    print("%.2f"%(avg))
