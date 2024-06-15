def calDegrees(sname):
    sName=[sname.count(x) for x in sname]
    return max(sName)
     


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

