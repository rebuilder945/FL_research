import random
def maxsum(lst):
    a = []
    for x in range(len(lst)//2):
        b = random.sample(lst,2)
        lst.remove(b[0])
        lst.remove(b[1])
        a.append(sum(b))
    return max(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

