def calDegrees(li):
       m = [li.count(x) for x in set(li)]
       return max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

