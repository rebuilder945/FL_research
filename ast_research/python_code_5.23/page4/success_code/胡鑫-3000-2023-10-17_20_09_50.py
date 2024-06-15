nums = eval(input())
avg = sum(nums)/len(nums)
if avg-int(avg) > 0:
    print("%.2f"%(avg))
else:
    print("%.2f"%(int(avg)))
