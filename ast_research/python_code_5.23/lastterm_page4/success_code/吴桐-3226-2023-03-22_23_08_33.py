def search(nums):
    for i in nums:
        cishu=nums.count(i)
        if cishu>len(nums)//2:
            return i
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


