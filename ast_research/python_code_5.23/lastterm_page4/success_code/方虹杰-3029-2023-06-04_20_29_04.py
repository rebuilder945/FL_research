a=eval(input())
for x in a:
    if a.count(x)>len(a)//2:
        b=x
    else:
        b="False"
print(b)
