items=input("")or"ok"
s={}
while items!='ok':
    a,b=items.split(' ')
    b=int(b)
    s[a]=b
    items=input("")or"ok"
print(list(s.keys()).sort())
print(list(s.values()).sort())
if 'India'  in s:
    print("yes")
else:
    print("no")
print(sum(list(s.values())))            
    



