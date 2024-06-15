a=eval(input())
s=[]
for i in a:
    for x in range(2,i+1):
        if i%x != 0:
            s.append(i)
print(s)            
