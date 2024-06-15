# 所谓“变位词”是指两个词之间存在组成字母的重新排列关系。如：heart和earth，python和typhon，1234与2134。

# 编程实现对输入的两个字符串判断是否为“变位词”，是输出True，不是输出False。

s = list(input())
n = list(input())
s.sort()
n.sort()
if s == n:
    print("Ture")
else:
    print("False")
