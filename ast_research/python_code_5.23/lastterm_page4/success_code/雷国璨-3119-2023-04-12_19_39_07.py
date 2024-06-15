a=eval(input())
a.reverse()
b=['']
for i in a:
    if i not in b:
        b.insert(0,i)
b.pop()
print(b)
