def search(nums):
    for i in nums:
        if nums.count(i) > int(len(nums))//2:
            return (i)





nums = eval(input())
y = search(nums)
print(y)


