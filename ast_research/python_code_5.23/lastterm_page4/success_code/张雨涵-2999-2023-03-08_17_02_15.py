a = str(input())
a1=a.split(" ")
b = input().split(" ")
n,m = b
n=eval(n)
m=eval(m)
a1[n],a1[m] = a1[m],a1[n]
print(a1)
# 善用split,split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）

