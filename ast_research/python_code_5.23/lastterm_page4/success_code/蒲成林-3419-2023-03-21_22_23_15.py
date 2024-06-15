from collections import Counter

def calDegrees(nums):
  # 创建一个Counter对象，统计列表中每个元素出现的次数
  counter = Counter(nums)
  # 找到字典中值最大的键对应的值，就是列表的度
  degree = max(counter.values())
  return degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

