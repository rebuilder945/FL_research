def calDegrees(a):
    list1=[]
    for x in a:
        b=a.count(x)
        list1.append(b)
     return max(list1)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

