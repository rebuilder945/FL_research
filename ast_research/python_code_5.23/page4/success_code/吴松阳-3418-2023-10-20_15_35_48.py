import random
def maxsum(lst):
    c = []
    for i in range(len(lst)**5):
        a = []
        for x in range(len(lst)//2):
            b = random.sample(lst,2)
            lst.remove(b[0])
            lst.remove(b[1])
            a.append(min(b))
        c.append(sum(a))
    return(max(c))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

