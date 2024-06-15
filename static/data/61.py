a = list(eval(input()))
n, m = eval(input())
c = len(a)

if n >= c:
    print("error")
else:
    b = a[n:n+1]
    #Python 中使用方括号来索引列表元素，而不是逗号
    for i in range(m):
    #使用了变量 b 来迭代，会覆盖之前定义的 b
        a.append(b[0])
    print(a)