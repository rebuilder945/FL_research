a=eval(input())
b=[]
for x in a:
    if x in b:
        b=b
    else:
        b.append(x)
   
print(b)
