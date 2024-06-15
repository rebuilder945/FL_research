a = input().split( )
b = {}
for i in a:
    b[i] = b.get(i,0)+1
print(max(b,key=b.get),end=" ")
print(max(b.values()))
