from tkinter import X


n = eval(input())
sb = [x for x in range(1,(n+1))]
for i in range(1):
    sb.append(sb[0])
    sb.remove(sb[0])
print(sb)
