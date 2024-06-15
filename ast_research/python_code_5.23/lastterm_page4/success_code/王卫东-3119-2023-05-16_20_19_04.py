a=eval(input())
a.reverse()
b=[]
for x in a:
    if x not in b:
        b.insert(0,x)
print(b)        
