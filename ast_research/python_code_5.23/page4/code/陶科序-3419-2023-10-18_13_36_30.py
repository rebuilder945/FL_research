def calDegrees(nums):
k =[]
b = (nums).split(",")
for i in (b):
    c = b.count(i)
    k.append(c)
    return(max(k))



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

