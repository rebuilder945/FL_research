nums=eval(input())
avg=sum(nums)/len(nums)
if sum(nums)%len(nums) == 0:
    print(int(avg))
else:
    pass
    print("%.2f" % avg)
