sb = eval(input())
x = sb.count(0)
while 0 in sb:
    if x > 0:
        sb.pop(0)
        sb.append(0)
        x = x-1
    else:
        continue
sb = sorted(sb)
print(sb)
