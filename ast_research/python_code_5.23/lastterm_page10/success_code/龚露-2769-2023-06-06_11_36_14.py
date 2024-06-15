a=input()
b=a[:]
print(b)
m={}
for x in a:
    if x.isalpha():
        m[x]=chr(25-ord(x))
        a.replace(x,m[x])
print(a)



    
    
