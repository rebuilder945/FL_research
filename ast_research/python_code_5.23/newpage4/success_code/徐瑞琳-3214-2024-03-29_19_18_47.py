sb = eval(input())
x = sb.count(0)
while 0 in sb:
    sb.pop(0)
for i in x:
    sb.append(0)
sb = sorted(sb)
print(sb)
