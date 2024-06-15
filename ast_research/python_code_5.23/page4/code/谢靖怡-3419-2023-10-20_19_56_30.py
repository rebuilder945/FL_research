def calDegrees(nums):
      dic={}
       for i in eval(input()):
            if i not  in dic:
            nums[i]=1
       else:
            nums[i]+=1
print max(dic.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

