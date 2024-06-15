m=eval(input())
n=m[::-1]
d=[]
for x in n:
    if x not in d:
        d.append(x)
print(d)


