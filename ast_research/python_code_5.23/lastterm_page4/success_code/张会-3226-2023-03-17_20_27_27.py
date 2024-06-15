def search(nums):
    a = nums/2
    b = 0
    for i in range(n):
        if nums.count(i) > a:
            b += nums[i]
    return b





nums = eval(input())
y = search(nums)
print(y)


