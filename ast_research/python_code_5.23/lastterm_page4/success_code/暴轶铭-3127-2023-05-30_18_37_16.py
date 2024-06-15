# #从键盘读入一个整数n, 并完成下述任务：
# 使用快速列表生成语法生成列表 [1, 2, ... ,n-1, n];
# 使用for循环将列表循环左移一个位置；
# 输出循环左移后的列表。
n = int(input())
lst = []
result = []
for i in range(1,n + 1):
    lst.append(i)
for x in lst:
    if x != lst[0]:
        result.append(x)
    else:
        pass
result.append(lst[0])
print(result)
