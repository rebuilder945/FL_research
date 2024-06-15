def max_sort(lt):
    # 将列表的长度赋值给变量n
    n = len(lt)
    # 使用冒泡排序(其他算法也可以，看自己喜欢的来)
    # 外层循环控制比较的轮数
    for i in range(n-1):
        # 内层循环控制比较的次数，每轮会确定排在列表末尾的一个值
        for j in range(n-1-i):
        # 每次将列表相邻两个元素转换成字符串使用+号连接起来，然后互换位置连接起来，再比较大小
            if str(lt[j])+str(lt[j+1]) < str(lt[j+1])+str(lt[j]):
             # 如果互换位置组合的数字大于初始位置组合的数字，则两个元素互换位置
                lt[j], lt[j+1] = lt[j+1], lt[j]
    # 当循环结束时，顺序已经排好，可以打印列表lt查看一下
    # 定义一个空字符串
    s = ''
    # 遍历排好序的列表
    for k in lt:
        # 将列表内的所有元素依次连接组合起来，返回时转换为数字类型
        s += str(k)
    return int(s)
m=eval(input())
print(max_sort(m))




