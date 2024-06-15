a=eval(input())
for i in a:
    if int(i)==0:
        b=a.pop(i)
        a.append(b)
print(list(a))
