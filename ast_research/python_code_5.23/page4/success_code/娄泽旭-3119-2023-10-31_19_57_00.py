a = eval(input())
b = []
for i in range(len(a)):
    if a[-i-1] not in b:
        b.append(a[-i-1])
b.reverse()
print(b)
