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

def havedigit(text):
    for i in text:
        if i.isdigit():
            return True
    return False
def havelowalpha(text):
    for i in text:
        if i.islower():
            return True
    return False
def haveupalpha(text):
    for i in text:
        if i.isupper():
            return True
    return False
def havespecial(text):
    ls=list("~!@#$%^&*()_=-/,.?<>;:[]{}|\\")
    for i in text:
        if i in ls:
            return True
    return False
pas=input()
level=0
if havedigit(pas):
    level+=1
if havelowalpha(pas):
    level+=1
if haveupalpha(pas):
    level+=1
if havespecial(pas):
    level+=1
if len(pas)>=8:
    level+=1
print(level)

