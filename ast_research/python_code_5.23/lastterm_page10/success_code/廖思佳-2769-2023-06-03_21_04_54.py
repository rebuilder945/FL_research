n=input()
s=""
for i in n:
    if i.isalpha() and ord(i)>=97:
        s=s+chr(122-ord(i)+97)
    elif i.isalpha() and 65<=ord(i)<=90:
        s=s+ chr(90-ord(i)+65)  
    else:
        s=s+i
print(n)
print(s)             
