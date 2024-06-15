a=input()
b='abcdefghijklmnopqrstuvwxyz'
for x in a:
    if x.isalpha():
        i=b.index(x.lower())+1
        print(chr(ord(x)+26-2*i+1),end='')
    else:
        print(x,end='')
print(a)
        
