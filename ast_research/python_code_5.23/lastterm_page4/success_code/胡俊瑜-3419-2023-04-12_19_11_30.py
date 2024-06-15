
freq=collections.Counter(nums)
max_freq=max(freq.values())
d=len([x for x in freq.keys()if freq[x]==max_freq])



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

