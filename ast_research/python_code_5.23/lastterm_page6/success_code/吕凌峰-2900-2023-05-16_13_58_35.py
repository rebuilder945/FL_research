# 回文素数
# 【问题描述】编写程序，从键盘输入一个数n，输出n以内的所有的回文素数
# 若n输入不合法（为小数或者负数），则输出提示：“illegal input”。
# 回文素数是指一个数既是素数又是回文数
# 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数称之为素数
# 例如131既是素数又是回文数。
def sushu(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def huiwenshu(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] == s[(-i) + (-1)]:
            return True
        else:
            return False

def huiwensushu(n):  # n is a list
    Output = []
    for x in n:
        if sushu(x) and huiwenshu(x):
            Output.append(x)
    Output.sort()
    for i in range(len(Output)):
        print(Output[i], end=' ')
    print(Output[-1])

n = eval(input())
if type(n) == int and n > 0:
    nums = [x for x in range(1, n + 1)]
    huiwensushu(nums)
else:
    print('illegal input')
