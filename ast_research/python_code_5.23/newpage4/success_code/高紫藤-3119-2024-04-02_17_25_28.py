a = eval(input())
b = []
for c in a:
    d = c.count()
    if d > 1:
        c.pop()
        b.append(c)
    elif d == 1:
        b.append(c)
print(b)

# a = eval(input())
# b = []
# for c in a:
#     if c not in b:
#         b.append(c)









