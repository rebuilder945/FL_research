# 密码强度
# 【问题描述】   
#     编写程序，对输入的密码（长度不超过28）进行强度检测。密码强度规定为：
#     1）含有数字字符；
#     2)含有小写字母； 
#     3）含有大写字母；
#     4）密码长度不低于8；
#     5）至少含有~!@#$%^&*()_=-/,.?<>;:[]{}|\中的一个字符
#     规定密码满足上列任意条件即加一星，程序输出密码的星级
# 【输入形式】
#   长度在28以内的任意字符串。
# 【输出形式】
#     根据密码强度要求，输出密码强度星级，用整数表示
# 【样例输入】
# 123.aq.Aw!
# 【样例输出】
# 5

def checkpw(s):
    stars = 0
    if len(s) >= 8:
        stars += 1
    letter, LETTER, nums, others = 0, 0, 0, 0 
    for i in s:
        if i.islower():    #小写英文字母ASCII码范围
            letter += 1
        elif i.isupper():    #大写英文字母ASCII码范围
            LETTER += 1
        elif i.isdigit():   #数字0-9字母ASCII码范围
            nums += 1
        else:
            others += 1
    if letter > 0:
        stars += 1
    if LETTER > 0:
        stars += 1
    if nums > 0:
        stars += 1
    if others > 0:
        stars += 1
    return stars

password = input()
print(checkpw(password))
