from os import remove


sb = eval(input())
x = eval(sb.count(0))
for i in range(0,(x+1)):
    remove(0)
    sb.append(0)
