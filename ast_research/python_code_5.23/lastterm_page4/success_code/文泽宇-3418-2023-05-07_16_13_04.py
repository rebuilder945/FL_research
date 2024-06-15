def maxsum(sb):
    sbb=sorted(sb)
    sbbb=sbb[::2]
    return(sum(sbbb))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

