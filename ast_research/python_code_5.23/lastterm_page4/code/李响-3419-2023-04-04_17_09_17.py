from collection import Counter
def calDegrees(nums) :
     nums = list(nums)
     d = Counter(nums)
     max_d = max(d.values())
     return max(k for k , v in d.items() if v == max_d



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

