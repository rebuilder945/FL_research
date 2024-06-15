def most_frequent(list):
  return max(set(list), key=list.count)
A = eval(input())
C = most_frequent(A)
print(A.count(C))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

