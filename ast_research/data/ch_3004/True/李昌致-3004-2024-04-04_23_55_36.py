import math
def is_prime(x):
    if x <= 1:
        return False # 如果输入的数字小于或等于1，返回False，因为素数必须大于1
    if x == 2:
        return True # 如果输入的数字是2，返回True，因为它是素数
    if x % 2 == 0:
        return False # 如果输入的数字是偶数（除了2），返回False，因为除了2以外的偶数都不是素数
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False # 如果输入的数字能被i整除，返回False，因为素数不能被这些数字整除
    return True # 如果输入的数字未被整除，返回True，表示它是素数

list = eval(input())
i = 0
newlist = []
for i in range(0,len(list)):
    if is_prime(list[i]):
        newlist.append(list[i])
print(newlist)
