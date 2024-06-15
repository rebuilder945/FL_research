def calDegrees(list):
    a=max(set(list),key=list.count)
    return list.count(a)
#https://baijiahao.baidu.com/s?id=1716217424688095831&wfr=spider&for=pc


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

