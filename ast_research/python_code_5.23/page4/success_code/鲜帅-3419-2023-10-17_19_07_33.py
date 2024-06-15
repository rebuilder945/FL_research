a = []
def calDegrees(lst):
    for x in lst:
        a.append(lst.count(x))
    return max(a)
    
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

