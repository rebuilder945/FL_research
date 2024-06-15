#list.copy() takes no arguments (1 given)
#list.copy() 方法不接受参数，它只是返回列表的一个副本。因此，a.copy(n) 会导致错误。
a = list(eval(input()))
n, m = eval(input())
c = len(a)

if n > c:
    print("error")
else:
    b = a.copy()
    for i in range(m):
        a.append(i)
        print(a)