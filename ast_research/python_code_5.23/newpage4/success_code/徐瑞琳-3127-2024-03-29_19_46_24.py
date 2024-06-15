from tkinter import X


n = eval(input())
sb = [x for x in range(1,(n+1))]
for i in range(0,(n)):
    sb.append(sb[1])
    sb.remove(sb[1])
print(sb)
