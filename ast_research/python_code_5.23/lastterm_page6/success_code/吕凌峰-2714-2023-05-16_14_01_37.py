# 成绩转换
# 【问题描述】
# 本题要求编写程序输入一个百分制成绩并把其转换为五分制成绩输出。
# 转换规则为：
# 大于等于90分为A；小于90且大于等于80为B；小于80且大于等于70为C；
# 小于70且大于等于60为D； 小于60为E。

def achievement_trans(x):
    if x >= 90:
        print('A')
    elif x >= 80 and x < 90:
        print('B')
    elif x >= 70 and x < 80:
        print('C')
    elif x >= 60 and x <70:
        print('D')
    elif x < 60:
        print('E')
achievement = eval(input())
achievement_trans(achievement)
