# 本题要求编写程序输入一个百分制成绩并把其转换为五分制成绩输出。

# 转换规则为：

# 大于等于90分为A； 小于90且大于等于80为B； 小
# 于80且大于等于70为C； 小于70且大于等于60为D； 小于60为E。

n = eval(input())
if n >=90:
    print("A")
elif 80<=n<90:
    print("B")
elif 70<=n<80:
    print("C")
elif 60<=n<70:
    print("D")
elif n<60:
    print("E")

