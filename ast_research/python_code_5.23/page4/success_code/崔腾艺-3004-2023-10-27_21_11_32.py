a=eval(input())
b=[2,3]
for x in a:
    if x!=1 and x%2!=0 and x%3!=0:
        b.append(x)
    else:
        pass
print(b)
