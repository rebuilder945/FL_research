lis1=[]
def maxsum(lie):
    for x in lie:
        for y in lie:
            if not x == y:
                a = x+y
                lis1.append(a)
    da=max(lis1)
    return da




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

