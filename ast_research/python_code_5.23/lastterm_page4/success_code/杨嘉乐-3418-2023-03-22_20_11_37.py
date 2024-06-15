def maxnums(aa):
    sum=0
    for x in aa:
        bb=aa
        bb.remove(x)
        for y in bb:
            if x+y>sum:
                sum=x+y
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

