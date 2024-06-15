import random


def rand_list(list):
        list_temp=[i for i in range(len(list))]
        list_new=random.sample(list_temp,len(list_temp))
        list_object=[list[i] for i in list_new]
        return list_object

def maxsum(nums):
    b = []
    for i in range(20):
        rnums = rand_list(nums)
        num = []
        i=0
        while i+1 < len(nums):
            a = [rnums[i],rnums[i+1]]
            x = min(a)
            num.append(x)
            i+=2
        b.append(sum(num))
    return max(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

