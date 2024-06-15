def maxsum(list1):
  list1.sort()
  sum=0
  for i in range(len(list1)):
      if i%2==0:
          sum=sum+list1[i]
return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

