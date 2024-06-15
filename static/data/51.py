a = eval(input())
a.sort(reverse=True)  # 使用 reverse=True 而不是 reserve=True
s = ''
for x in a:
    s = s + str(x)
s = int(s)
print(s)