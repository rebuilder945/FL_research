nums = eval(input())
nums.sort()
a = [int(nums[i])*10**i for i in range(0,len(nums))]
b=sum(a)
print(b)
