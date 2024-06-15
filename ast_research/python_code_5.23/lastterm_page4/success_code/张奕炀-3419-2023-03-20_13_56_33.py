def calDegrees(s):
    k = 0
    for i in range(len(s)):
        if s.count(i) > k:
            k = i
    return(k)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

