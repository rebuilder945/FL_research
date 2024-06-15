def calDegrees:
      counts={}
       for num in numes:
           counts[num]=counts.get(num,o)+1
       degree=max(counts.values())
        return degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

