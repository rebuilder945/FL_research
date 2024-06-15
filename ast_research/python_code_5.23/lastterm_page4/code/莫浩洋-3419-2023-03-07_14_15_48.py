b=['0']
def calDegrees(x)
       for i in x:
          a=nums.count(i)
          b.append(a)
       return max(b)
     
     


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

