a=eval(input())
b=[]
for i in a[::-1]:
    if i not in b:
        b.append(i)
b.reverse()
print(b)
