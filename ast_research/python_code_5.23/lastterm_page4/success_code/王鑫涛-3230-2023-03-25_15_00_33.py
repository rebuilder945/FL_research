a= list(eval(input()))
a.sort(reverse=True)
if a[-1] in [0]:
    while a[-1] in [0]:
        a.pop(0)
        continue
    a.append(0)
else:
    pass
b=''.join(str(i) for i in a)
print(b)
