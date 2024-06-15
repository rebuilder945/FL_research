n = eval(input())
sb = [x+1 for x in range(1,(n+1))]
for i in sb:
    sb.append(i)
    sb.remove(i)
print(sb)
