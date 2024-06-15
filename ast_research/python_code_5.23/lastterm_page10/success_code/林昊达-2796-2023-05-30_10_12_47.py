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

def find1stmax(ls):
    max=0
    for i in ls:
        if len(i)>max:
            max=len(i)
    for i in ls:
        if len(i)==max:
            return i


text=input()
for i in text:
    if i.isdigit():
        break
else:
    print("No digits")
text2=""
for i in text:
    if i.isdigit():
        text2+=i
    else:
        text2+=" "
text2=text2.split()
text2.reverse()
for i in text2:
    if i==find1stmax(text2):
        print(i)
        break
