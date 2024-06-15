sb = eval(input())
for i in sb:
    x = sb.count(i)
    if x>1:
        for i in range(x):
            sb.remove(i)
    else:
        continue
print(sb)
