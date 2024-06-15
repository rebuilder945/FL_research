a=input()
b=[]
for i in a:
    for x in range(2,10):
        if i/x in range(2,10):
            b.append(i)
        else:
            break
print(b)            
