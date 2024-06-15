def calDegrees(a):
    from collections import Counter
    b=Counter(a).most_common(1)[0][1]
    return(b)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

