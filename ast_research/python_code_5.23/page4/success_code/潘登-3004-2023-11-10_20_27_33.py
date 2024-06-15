a=eval(input())
s=[]
for x in a :
    if x>2:
        for i in range(2,x):
            if x%i != 0:
                s.append(x)
                break
            else:
                continue            
print(s)
