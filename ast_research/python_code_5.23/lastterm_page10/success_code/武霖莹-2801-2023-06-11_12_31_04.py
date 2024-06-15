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
a=input()
lst1="\~!@#$%^&*()_=-/,.?<>;:[]}{|"
lst2="1234567890"
jishu=0
for i in a:
    if i in lst2:
        jishu+=1
        break
for i in a:
    if i.islower():
        jishu+=1
        break
for i in a:
    if i.isupper():
        jishu+=1
        break
if len(a)>=8:
    jishu+=1
for i in a:
    if i in lst1:
        jishu+=1
        break
print(jishu)

