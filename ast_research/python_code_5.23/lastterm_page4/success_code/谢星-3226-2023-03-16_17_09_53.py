def search(nums):
    for i in nums:
        k = nums.count(i)
    if k<=len(nums)//2:
        return False
    else :
        return i





nums = eval(input())
y = search(nums)
print(y)


