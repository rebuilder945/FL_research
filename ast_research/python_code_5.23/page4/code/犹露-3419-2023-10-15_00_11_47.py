def calDegrees(n)：
n_stat = {}
for i in set(n):
     n_stat[i] = n.count(i)
     b =  max(n_stat,key = n.count)
     return b



return 


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

