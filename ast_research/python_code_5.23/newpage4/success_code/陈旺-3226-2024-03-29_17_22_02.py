def search(nums):
    n = len(nums)
 
    for y in nums:
        # 当element等于i，返回1，将返回的1累加统计num的出现次数
        count = sum(1 for element in nums if element == i)
        if count >= math.ceil(n/2):
            return y





nums = eval(input())
y = search(nums)
print(y)


