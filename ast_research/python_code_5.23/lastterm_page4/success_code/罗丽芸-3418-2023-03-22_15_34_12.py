def maxsum(sums):
          sums.sort()
          new=sum[0:len(sums):2]
          h=sum(new)
          return  h;




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

