a = eval(input())
a.sort(reverse=True)
b = ""
for i in range(len(a)):
    c = str(a[i])
    b = b + c

if b.count('0') == len(b):
#检查字符串 b 中是否全是字符 '0'，使用了 0 而不是字符串 '0'。
    print(0)
else:
    print(b)