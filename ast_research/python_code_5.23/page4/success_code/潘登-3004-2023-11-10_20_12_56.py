a=eval(input())
s=[]
for i in range(a):
    for x in range(i+1):
        if i % x != 0:
            s.append(i)
print(s)            
