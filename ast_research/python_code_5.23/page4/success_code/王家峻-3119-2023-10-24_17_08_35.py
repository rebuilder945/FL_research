n=eval(input())
b=[]
[b.append(i) for i in n if not i in b]
print(b)
