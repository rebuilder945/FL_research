word = input()
print(word)
list = []
for s in word:
    if s.isalpha():
        if s.islower:
            a = chr(26-(ord(s)-96)+1+96)
            list.append(a)
        if s.isupper():
            a = chr(26-(ord(s)-64)+1+64)
    else:
        list.append(s)
print("".join(list))
         
