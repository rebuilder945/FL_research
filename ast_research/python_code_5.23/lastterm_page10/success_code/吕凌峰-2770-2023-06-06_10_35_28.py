# “变位词”判断
# 【问题描述】
#  所谓“变位词”是指两个词之间存在组成字母的重新排列关系
# 如：heart和earth，python和typhon，1234与2134。
# 编程实现对输入的两个字符串判断是否为“变位词”，是输出True，不是输出False。
# 【输入形式】
# 输入两个字符串，一行一个字符串
# 【输出形式】
# 输出逻辑True或False
# 【样例输入】
# heart
# earth
# 【样例输出】
# True

def bianwei(s, m):
    for i in s:
        if  s == m or i not in m or s.count(i) != m.count(i):
            return False
    return True

a = input()
b = input()
print(bianwei(a, b))
