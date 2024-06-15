# 删除子串
# 【问题描述】
# 编写一个程序，当在一个字符串中出现指定子串时就删除它。
# 【输入形式】
# 用户在第一行输入一个字符串，用户在第二行输入一个子串。
# 【输出形式】
# 程序在下一行输出删除其中所有子串后的字符串。
# 如果字符串不包含子串则输出原字符串本身。
# 【样例输入】
#  I am a boy!
#  a             
# 【样例输出】
#  I#m##boy!       
# 【样例说明】用户首先输入字符串I am a boy!,
# 然后输出子串a,程序会寻找字符串中的子串删除它，最后
# 将删除后的结果输出:I#m##boy!   #表示空格。



def delstring(s1, s2):
    Output = ""
    while s2 in s1:
        a = s1.index(s2)
        Output += s1[0 : a]
        s1 = s1[a + len(s2): len(s1) + 1]
    Output += s1
    return Output



s1 = input()
s2 = input()
print(delstring(s1, s2))
