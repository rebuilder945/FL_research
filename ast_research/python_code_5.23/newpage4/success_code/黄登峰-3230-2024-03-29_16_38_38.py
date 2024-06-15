a=eval(input())
b=[]
for x in a:
    if x not in b:
        b.append(x)
b.sort(reverse=True)
print("".join(str(x) for x in b))
