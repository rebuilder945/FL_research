a = eval(input())
n, m = map(int, eval(input()))
#int() 函数无法直接将元组作为参数。将 eval(input()) 的结果拆包为两个整数变量。
b = []
b += a

if n <= len(a) - 1:
#len(a-1) 的语法是不正确的。获取列表 a 的长度，并与 n-1 进行比较。
    for _ in range(m):
    #m 是一个整数，不支持迭代。需要使用 range(m) 来实现循环。
        b.append(a[n])
        #将列表 a 的第 n 个元素添加到列表 b 中，应该使用 a[n] 而不是 a(n)。
    print(b)
else:
    print('error')