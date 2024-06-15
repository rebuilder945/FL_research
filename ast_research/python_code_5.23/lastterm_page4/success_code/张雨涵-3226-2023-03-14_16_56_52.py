def search(nums):
    n = len(nums)
    for i in nums:
        t = nums.count(i)
        if t > n//2 :
            h = i
        else:
            h = "False"
    return h





nums = eval(input())
y = search(nums)
print(y)


