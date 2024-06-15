def k(x):
    if x <= 1:
        return False  # 如果输入的数字小于或等于1，返回False，因为素数必须大于1
    for i in range(2, x):
        if x % i == 0:
            return False # 如果输入的数字能被i整除，返回False，因为素数不能被这些数字整除
        else:
            return True # 如果输入的数字未被整除，返回True，表示它是素数
num=eval(input())
b=[]
for x in num:
    if k(x):
        b.append(x)
print(b)
