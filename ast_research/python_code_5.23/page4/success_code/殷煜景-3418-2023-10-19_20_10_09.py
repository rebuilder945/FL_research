def maxsum(lb):
    lb=lb.sort()
    for i in len(lb)/2:
        lb1=lb.pop(0,1)
        lb2=list(eval(min(lb1)))
    return sum(lb2)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

