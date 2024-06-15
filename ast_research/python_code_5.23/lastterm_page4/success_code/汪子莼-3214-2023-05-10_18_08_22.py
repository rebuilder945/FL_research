a=eval(input())
for i in a:
    if i==int(0):
        b=a.pop(i)
        a.append(b)
print(list(a))
