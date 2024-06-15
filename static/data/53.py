import random

nums = eval(input())
ls1 = []

a, b = random.sample(ls1, 2)
#[ls1] 应该是 ls1，因为 random.choice() 函数期望一个可迭代对象，而不是一个包含列表的列表
#random.choice() 函数不支持 size 关键字参数。如果想从列表中选择多个元素，可以使用 random.sample() 函数
c = min(a, b)

ls2 = []
for i in range(0, len(ls2)):
#循环中，使用了 c 作为循环变量，但在循环内部又将其用作了其他用途。这会导致混淆
    nums += ls2[i]

ls3 = []

def maxsum(nums):
    return max(nums)
#在调用 maxsum(nums) 函数之前，定义该函数

v = maxsum(nums)
print(v)