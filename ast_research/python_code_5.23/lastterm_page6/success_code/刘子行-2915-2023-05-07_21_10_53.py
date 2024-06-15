n = int(input())
nar_num = []

# 检查每个小于等于n的三位数是否是水仙花数
for num in range(100, n + 1):
    i, j, k = map(int, str(num))  # 分离每个三位数的百、十、个位数字
    if num == i**3 + j**3 + k**3:
        nar_num.append(num)

# 输出结果
if len(nar_num) == 0:
    print("none")
else:
    for num in nar_num:
        print(num)
