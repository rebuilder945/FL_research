def calDegrees(ak):
    z=0
    for x in ak:
        if ak.count(x)>z:
            z=ak.count(x)
    return z

    



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

