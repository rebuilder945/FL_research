a=eval(input())
for i in a:
    if int(i)==0:
        a.remove(0)
        a.append(0)
print(a)
