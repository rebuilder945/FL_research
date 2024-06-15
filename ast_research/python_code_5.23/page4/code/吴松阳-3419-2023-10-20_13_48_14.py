def calDegrees(i):
    d = i.count(max(i,key = i.count))
return d
        


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

