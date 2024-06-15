a=eval(input()).reverse()
b=[]
for x in a:
    if x not in b:
        b.append(x).reverse()
print(b)



