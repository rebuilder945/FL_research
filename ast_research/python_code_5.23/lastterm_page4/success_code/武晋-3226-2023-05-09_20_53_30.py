def search(nums):
    for i in nums:
        s=0
        if (nums.counts(i))>(len(nums)//2):
            return i
    return False
             





nums = eval(input())
y = search(nums)
print(y)


