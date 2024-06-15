n = eval(input())
lst = []
s = 0        #存储最长的字符串长度
long = ''    #最长的字符串
for i in range(n):
    lst.append(input())
for ch in lst:
    if len(ch) > s:
        s = len(ch)
        long = ch
print(long)
