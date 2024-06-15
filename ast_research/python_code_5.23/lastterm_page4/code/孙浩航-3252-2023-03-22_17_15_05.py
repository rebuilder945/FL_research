def fibonacci(n):
&#160; &#160; """
&#160; &#160; 获取斐波那契数列第n项的值
&#160; &#160; :param n: 斐波那契数列的项数，从1开始计数
&#160; &#160; :return: 第n项的斐波那契数列的值
&#160; &#160; """
&#160; &#160; if n <= 0:
&#160; &#160; &#160; &#160; return None
&#160; &#160; if n == 1 or n == 2:
&#160; &#160; &#160; &#160; return 1
&#160; &#160; else:
&#160; &#160; &#160; &#160; return fibonacci(n - 1) + fibonacci(n - 2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


