a=input()
b=input()
words=a.split()
for i in words:
    if b in words:
        words.remove(b)
print("".join(str(x) for x in words))
