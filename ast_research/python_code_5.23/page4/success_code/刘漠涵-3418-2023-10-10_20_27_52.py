def maxsum(numbers):
    numbers=list(numbers)
    numbers.sort(reverse=False)
    a=sum(numbers[0:-1:2])
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

