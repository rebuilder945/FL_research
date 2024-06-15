def search(nums):
    k = 0
    for i in nums:
        if nums.count(i) > k :
            k = nums.count(i)
    if k<=len(nums)//2:
        return False
    else :
        for i in nums:
            if nums.count(i)==k :
                return i





nums = eval(input())
y = search(nums)
print(y)


