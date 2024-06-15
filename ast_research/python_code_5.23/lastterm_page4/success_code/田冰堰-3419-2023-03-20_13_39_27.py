def calDegrees(d):
    for x in d:
        if(d.count(x)>len(d)):
            return x;
        return False

           



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

