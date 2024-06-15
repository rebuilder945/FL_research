def search(nums):
    for x in nums:
        if nums.count(x)>n//2:
            return x
        else:
            return Flase





nums = eval(input())
y = search(nums)
print(y)


