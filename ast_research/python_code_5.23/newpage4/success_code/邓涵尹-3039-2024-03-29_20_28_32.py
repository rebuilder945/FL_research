#nums = eval(input())
#for num in nums:
#    if nums.count(num) > 1:
#        a = nums.pop(num)
#    else:
#        nums.append("num")
#print(nums)

nums = eval(input())

nums.sort()
del nums[0]
del nums[-1]

print(nums)
