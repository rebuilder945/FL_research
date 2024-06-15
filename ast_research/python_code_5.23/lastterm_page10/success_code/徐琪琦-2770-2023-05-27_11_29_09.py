#  所谓“变位词”是指两个词之间存在组成字母的重新排列关系。如：heart和earth，python和typhon，1234与2134。
# 编程实现对输入的两个字符串判断是否为“变位词”，是输出True，不是输出False。
a = input()
b = input()
b = list(b)
def bianweici(a,b):
    if len(a) != len(b) or a == b:
        return False
    else:
        for i in a:
            if i not in b:
                return False
            else:
                if a.count(i) >1:
                    if a.count(i) != b.count(i):
                        return False
        return True

print(bianweici(a,b))


