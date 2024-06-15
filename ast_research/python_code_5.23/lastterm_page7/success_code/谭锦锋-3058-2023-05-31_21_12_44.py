x = {}
s = input()
while s!='q':
    x[s]=x.get(s,0)+1
    s=input()
print(max(x,key=x.get),end=" ")
print(max(x.values()))
