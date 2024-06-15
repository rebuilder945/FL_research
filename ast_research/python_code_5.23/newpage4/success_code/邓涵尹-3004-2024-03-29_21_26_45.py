def ps(nums):
    c={}
    for num in nums:
        for b in range(1,10000):
            if num % b == 0:
                del nums[num]
            else:
                nums.append(num)

nums = eval(input())
print(ps(nums))
