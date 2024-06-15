a = eval(input())
b = []
for x in a:
    if x>=2:
        for c in range(2,x,1):
            if x%c == 0:
                break
            else:
                b.append(x)
print(b)                
    

