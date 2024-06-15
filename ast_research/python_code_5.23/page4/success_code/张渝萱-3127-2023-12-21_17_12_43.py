a = eval(input())
# 创建快速列表！但是为什么是a+1啊？？？
list1 = list(range(1,a+1))
num = 0
n = 0
for x in list1:
    if num == 0:
        n = x
        list1[num] = list1[num+1]
        num += 1
    elif num == len(list1)-1:
        list1[num] = 1
        break
    else:
        list1[num] = list1[num + 1]
        num += 1
print(list1)
