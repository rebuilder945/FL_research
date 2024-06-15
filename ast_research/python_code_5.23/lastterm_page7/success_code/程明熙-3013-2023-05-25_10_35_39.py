# 获取国家的GDP值(字典-1)
# 【问题描述】
# 存储国家GDP的字典结构如下：
# GDP = {
# 'USA': 95,
# 'China': 80,
# 'Japan': 50
# }
# 题目要求：
# 1、请从标准输入录入多个国家的名字和对应的GDP，存入GDP字典中。(字典不为空)
# 2、获取所有的key值，存储在列表里
# 3、获取所有的value值，存储在列表里
# 4、判断 键'India' 是否在字典中
# 5、获得字典里所有value 的和

lst = input().split()
dic = {}
while lst != ['ok']:
    dic['%s'%(lst[0])] = int(lst[1])
    lst = input().split()
Countries = []
GDP = []
Sum = 0
for x, y in dic.items():
    y = int(y)
    Countries.append(x)
    GDP.append(y)
    Sum += y
Countries.sort()
GDP.sort()
print(Countries)
print(GDP)
if 'India' not in dic:
    print('no')
else:
    print('yes')
print(Sum)
