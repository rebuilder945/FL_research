def maxsum(s):
    sum = 0
    s.sort(reverse = False)
    for i in range(len(s)):
        if i%2 == 0:
            sum += s[i]
    return sum
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

