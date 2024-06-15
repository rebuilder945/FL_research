a=list(input())
b=a.copy()
c=0
d=["~",'!','@','#','$','%','^','&','*','()','_','=','-','/',',','.','?','<>',';',':','[]','{}','|','\\']
if len(a)>=8:
    c+=1
for i in a:
    if i.isdigit():
        c+=1
        for i in b:
            if i.isdigit():
                a.remove(i)
for i in a:
    if i.islower():
        c+=1
        for i in b:
            if i.islower():
                a.remove(i)  
for i in a:    
    if i.isupper():
        c+=1
        for i in b:
            if i.isupper():
                a.remove(i)  
for i in a:
    if i in d:
        c+=1
        for i in b:
            if i in d:
                a.remove(i)
print(c)


