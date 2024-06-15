def search(nums):
    b1 = []
    b2 = []
    for i in nums:
        t = nums.count(i)
        if t > len(nums) // 2:
            b1.append(t)
        if b1 == []:
            return False
        else:
            return max(b1)





nums = eval(input())
y = search(nums)
print(y)


