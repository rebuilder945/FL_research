def maxsum(lst):
    ls=sorted(lst)
    suml=0
    for x in range(0,len(lst),2):
        suml+=lst[x]




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

