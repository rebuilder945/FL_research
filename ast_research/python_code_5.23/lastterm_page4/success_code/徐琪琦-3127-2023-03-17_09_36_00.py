#从键盘读入一个整数n, 并完成下述任务：
# 使用快速列表生成语法生成列表 [1, 2, ... ,n-1, n];
# 使用for循环将列表循环左移一个位置；
# 输出循环左移后的列表。
n = eval(input())
list1 = []
for i in range(n):
    list1.append(i+1)
a = list1.pop(0)
list1.append(a)
print(list1)

