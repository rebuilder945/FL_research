mima = input()
jiema = ""
zheng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
fan = zheng[::-1]

for x in mima:
    if x.isalpha():
        index = zheng.find(x)
        jiema += fan[index]
    else:
        jiema += x

print(mima)
print(jiema)
