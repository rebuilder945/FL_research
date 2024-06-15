mima = input()
jiema = ""
zheng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
fan = "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"

for x in mima:
    if x.isalpha():
        index = zheng.find(x)
        jiema += fan[index]
    else:
        jiema += x

print(mima)
print(jiema)
