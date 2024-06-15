a=input()
b='abcdefghijklmnopqrstuvwxyz'
ls=[]
for x in a:
    if x.isalpha():
        i=b.index(x.lower())+1
        c=chr(ord(x)+26-2*i+1)
        ls.append(c)
    else:
        ls.append(x)
print(''.join(ls))
print(a)
        
