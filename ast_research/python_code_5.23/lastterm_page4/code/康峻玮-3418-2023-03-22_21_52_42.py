def maxsum
    list = nums
    list.sort()
    b = list[::2]
    c = maxsum(b)
return maxsum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

