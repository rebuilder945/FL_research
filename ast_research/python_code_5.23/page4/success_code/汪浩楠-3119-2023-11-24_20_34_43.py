a=eval(input())
b=[]
for i in a[::-1]:
    if i not in b:
        b.insert(0,i)
print(b)
