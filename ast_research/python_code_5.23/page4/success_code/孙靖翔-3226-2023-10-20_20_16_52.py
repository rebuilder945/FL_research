def search(nums):
    for n in nums:
        if nums.count(n)>len(nums):
            return n
        else:
            return False






nums = eval(input())
y = search(nums)
print(y)


