def most_frequent(list):
  a = max(set(list), key=list.count)
  return list.count(a)
num = eval(input())
d = most_frequent(num)
print(d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

