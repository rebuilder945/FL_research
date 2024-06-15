def find_degree(nums):
      freqc= {}
      degree = 0
      for num in nums:
            if num not in freq:
                  freq[num] = 1
            else:
                  freq[num] += 1
            degree = max(degree, freq[num])
      return degree



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

