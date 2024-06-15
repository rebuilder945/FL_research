def calDegrees(d):
    for x in d:
        if(d.count(x)>(len(d)//2)):
            return False;



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

