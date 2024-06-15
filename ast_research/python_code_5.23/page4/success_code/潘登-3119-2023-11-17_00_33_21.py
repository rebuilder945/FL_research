a=eval(input())
a.reverse()
b=[]
for x in range(a):
    if x not in b:
        b.append(a)
b.reverse()
print(b)        
