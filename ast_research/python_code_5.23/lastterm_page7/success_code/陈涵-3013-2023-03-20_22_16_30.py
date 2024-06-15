items=input("")or"ok"
s={}
while items!='ok':
    a,b=items.split(' ')
    b=int(b)
    s[a]=b
    items=input("")or"ok"
print(list(s.keys()))
print(list(s.values()))
if 'India'  in s:
    print("ok")
else:
    print("no")
print(sum(list(s.values())))            
    



