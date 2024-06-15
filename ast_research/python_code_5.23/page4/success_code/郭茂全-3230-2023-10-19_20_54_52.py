list=eval(input())
a=[str(x) for x in list]
for x in a:
    x+=x
print(x)
