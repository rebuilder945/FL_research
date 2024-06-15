a = input()
x = {}
while a != "q":
    x[a] = x.get(a,0) + 1
    a = input()
print(max(x,key=x.get),end=" ")  
print(max(x.values()))
