# 字符串中的最长数字子串
# 【问题描述】
#     本题目要求读入一个字符串，输出字符串的最长数字子串。
# 【输入形式】
#     输入一个字符串
# 【输出形式】
#     输出最长数字子串，若有多个最长数字子串输出最后一个，若字符串无数字字符，则输出“No digits”。

# 【输入样例】
# sdffsd123werrer456fgdgdg1dfgdf12
# 【样例输出】
#   456

def check(s):
    #判断是否是纯英文
    flag = False
    for x in s:
        if x.isdigit():
            flag = True
            break
    if not flag:
        return False
    else:
        return True

def findstr(s, dic, n):
    if not check(s):
        return dic
    #找所有的字串，并将其存入字典
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(i + 1, len(s)):
                if not s[j].isdigit():
                    if j != len(s) - 1:
                        dic["%s"%s[i:j]] = i + n
                        findstr(s[j:], dic, j)
            break
    #将字典中的数据处理


    # lst = []
    # for m, n in dic.items():
    #     lst.append([m, n])
    # print(lst)

def main():
    s = input()
    if not check(s):
        return "No digit"
    else:
        dic = {}
        findstr(s, dic, 0)

main()

