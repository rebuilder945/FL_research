a=list(input())
b=0
if len(a)>=8:
    b+=1
for x in a:
    if 48<=ord(x)<=57:
        b+=1
        break
for x in a:
    if 65<=ord(x)<=90:
        b+=1
        break
for x in a:
    if 97<=ord(x)<=122:
        b+=1
        break
c="\~!@#$%^&*()_=-/,.?<>;:[]{}|"
for x in a:
    if x in c:
        b+=1
        break
print(b)    

       
    
