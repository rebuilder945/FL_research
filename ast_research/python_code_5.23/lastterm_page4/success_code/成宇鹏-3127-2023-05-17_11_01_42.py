# 从键盘读入一个整数n, 并完成下述任务：

# 使用快速列表生成语法生成列表 [1, 2, ... ,n-1, n];

# 使用for循环将列表循环左移一个位置；

# 输出循环左移后的列表

n = int(input())
lst = [x for x in range(1,n+1)]
for x in lst:
    if lst.index(x) == 0:
        lst.remove(x)
        lst.append(x)
print(lst)

