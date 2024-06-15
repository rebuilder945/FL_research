# 【问题描述】

# 有一行电文，已按下面规律译成密码：

#      A--Z   a--z
#      B--Y   b--y

#      C--X   c--x

#      ......

# 即第1个字母变成第26个字母，第i个字母变成第（26-i+1）个字母; 非字母字符不变。编写程序把密码译回原文，并输出密码和原文。

# 【输入形式】

# 输入一串密码

# 【输出形式】

# 首先输出密码，然后换行后输出原文

# 【样例输入】

# 4sdf&13TBD

# 【样例输出】

# 4sdf&13TBD

# 4hwu&13GYW

etext=input()
text=etext
kl1="abcdefghijklmnopqrstuvwxyz"
kl2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ori=kl1+kl2
lk1=kl1[::-1]
lk2=kl2[::-1]
dec=lk1+lk2
for i in etext:
    if i in ori:
        text=text.replace(i,dec[ori.index(i)])
print(text)
print(etext)
