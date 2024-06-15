#编写程序，从键盘输入一个数n，输出n以内的所有的回文素数。
#若n输入不合法（为小数或者负数），则输出提示：“illegal input”。
#回文素数是指一个数既是素数又是回文数。
# 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数称之为素数。例如131既是素数又是回文数。
def huiwen(n):
    for i in str(n):
        for x in str(n).reverse:
            if i != x:
                return 0
    return 1
def sushu(n):
    for i in range(1,n):
        if n % i == 0:
            return 0 
    return 1
    
n = eval(input())
if type(n) == float or n < 0:
    print("illegal input")
else:
    for i in range(n):
        if huiwen(i) and sushu(i):
            print(i,end = " ")

