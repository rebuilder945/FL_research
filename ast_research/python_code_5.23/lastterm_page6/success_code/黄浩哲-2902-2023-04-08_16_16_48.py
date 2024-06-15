n = int(input(""))

a, b = 2, 1  # 初始化数列的前两项
sum = 0  # 初始化数列的前n项之和

for i in range(n):
    sum += a / b  # 累加数列的每一项
    a, b = a + b, a  # 计算数列的下一项

print("%.4f"%(sum))
