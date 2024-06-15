a = list(eval(input()))
b =[]
t = max(a)
s = min(a)
for i in a:
    if i !=t and i !=s:
        b.append(i)
print(b)
