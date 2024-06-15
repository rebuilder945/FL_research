def maxsum(y):
      y.sort(reserve=False);
      for i in range(len(y)):
      sum = 0;
      if (i+1)%2==0:
         sum+=y[i]+y[i-1]
     return sum;
      




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

