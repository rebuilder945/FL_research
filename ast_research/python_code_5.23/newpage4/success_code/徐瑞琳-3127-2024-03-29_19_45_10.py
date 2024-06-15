n = eval(input())
sb = [x+1 for x in range(1,(n+1))]
for i in sb:
    sb.append(sb[1])
    sb.remove(sb[1])
print(sb)
