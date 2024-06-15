n=0
s=0
while True:
    p=input()
    if p == '#':
       break
    s+=int(p)
    n+=1
print(n,s)
