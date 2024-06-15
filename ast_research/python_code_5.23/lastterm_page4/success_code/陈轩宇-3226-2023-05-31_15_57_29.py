def search(nums):
    for i in nums:
        jishu = nums.count(i)
        if jishu>len(nums)//2:
            return i
    return False





nums = eval(input())
y = search(nums)
print(y)


