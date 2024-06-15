s = input()  
a = 0 
b = 0 
c = 0 
d = 0  
for e in s:
    if e.isalpha():  
        a += 1
    elif e.isspace():  
        b += 1
    elif e.isdigit():
       c += 1
    else:
        d += 1  
print(a,b,c,d)
