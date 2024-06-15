a = list(eval(input()))
b = []
for i in a:
    if i > 1:
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            b.append(i)
            #b.append()这一行，需要一个缩进的代码块
print(b)