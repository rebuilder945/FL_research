list1 = eval(input())
n, m = map(int, input().split(','))

# 获取列表的最大值和最小值
max_val = max(list1)
min_val = min(list1)

# 检查 n 和 m 是否在列表的最大值和最小值之间
if min_val <= n <= max_val and min_val <= m <= max_val:
    # 获取要删除的元素的下标范围
    start_index = list1.index(n)
    end_index = list1.index(m)
    
    # 删除元素
    del list1[start_index+1:end_index]
    print(list1)
else:
    print("error")

