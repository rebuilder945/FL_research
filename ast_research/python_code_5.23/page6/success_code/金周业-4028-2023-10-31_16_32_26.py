"""
【问题描述】编写程序，从键盘输入一个数n，输出n以内的所有的回文素数。若n输入不合法（为小数或者负数），则输出提示：“illegal input”。
回文素数是指一个数既是素数又是回文数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数称之为素数。例如131既是素数又是回文数。
【输入形式】输入一个整数n（n>1）。
【输出形式】以空格分隔输出n以内的所有的回文素数。若n输入不合法（为小数或负数），则输出提示“illegal input”
【样例输入1】200
【样例输出1】2 3 5 7 11 101 131 151 181 191
【样例输入2】-4
【样例输出2】illegal input
"""
n = eval(input())
lst = []
if type(n) != int or n <= 0:  # 排除非整数类型和复数
    print("illegal input")
else:
    for i in range(1, n + 1):  # 找出回文数
        n = str(i)
        m = n[::-1]
        if int(n) == int(m):
            a = 0
            for x in range(1, i + 1):  # 找出素数
                if i % x == 0:
                    a = a + 1
            if a == 2:
                print(i, end=" ")

