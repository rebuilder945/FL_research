n=int(input())
a=[i for i in range(n+1)]
b=a
for x in range(0,1):
    b.append(b.pop(0))
print(b)
    

