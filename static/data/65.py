a = eval(input())
a.sort(reverse=True)

a = [str(num) for num in a]

#a 是一个包含整数的列表，在使用 join() 函数时，它期望的是字符串列表而不是整数列表。
#在排序后将整数列表中的每个整数转换为字符串，然后再使用 join() 函数将字符串连接起来输出。

print(''.join(a))