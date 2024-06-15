list1 = eval(input())
n, m = map(int, input().split(','))

# 检查 n 和 m 是否在列表下标范围内
if 0 <= n < len(list1) and 0 <= m < len(list1) and n <= m:
    del list1[n:m]
    print(list1)
else:
    print("error")

