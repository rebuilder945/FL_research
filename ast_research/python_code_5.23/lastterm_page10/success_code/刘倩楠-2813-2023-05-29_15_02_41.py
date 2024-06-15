a=input()
b=input()
words=a.split()
if b in words:
    words.remove(b)
print(words)
