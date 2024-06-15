a=eval(input())
numbers=list(a)
numbers.reverse()
b=[]
for x in numbers:
    if x not in b:
        b.append(x)
b.reverse()
print(b)
