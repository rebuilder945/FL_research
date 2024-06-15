def maxsum(list):
      a=sorted(list,reverse=True)
      n=len(a)
      x=a[1:n:2]
      b=sum(x)
      return b
      




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

