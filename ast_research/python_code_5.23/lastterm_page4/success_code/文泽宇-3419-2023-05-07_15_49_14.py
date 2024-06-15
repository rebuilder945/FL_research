def calDegrees(sb):
    lst=[sb.count(i) for i in sb]
    return(max(lst))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

