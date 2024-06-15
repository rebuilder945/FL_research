def calDegrees
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

