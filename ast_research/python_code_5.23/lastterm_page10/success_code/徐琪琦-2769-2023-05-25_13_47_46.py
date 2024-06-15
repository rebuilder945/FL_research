#有一行电文，已按下面规律译成密码：
#      A--Z   a--z
#      B--Y   b--y
#      C--X   c--x
#      ......
# 即第1个字母变成第26个字母，第i个字母变成第（26-i+1）个字母; 非字母字符不变。编写程序把密码译回原文，并输出密码和原文。
code = input()
print(code)
xiaoxie = []
daxie = []
for i in range(26):
    xiaoxie.append(chr(ord("a")+i))
for i in range(26):
    daxie.append(chr(ord("A")+i))
for i in code:
    if "a"<= i <= "z":
        i = xiaoxie[27-xiaoxie.index(i)]
        print(i,end = "")
    elif "A"<= i<= "Z":
        i = daxie[27-daxie.index(i)]
        print(i,end = "")
    else:
        print(i,end = "")
        

