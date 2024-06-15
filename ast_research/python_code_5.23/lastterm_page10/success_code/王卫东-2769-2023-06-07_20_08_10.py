n=input()
print(n)
for x in n:
    if 65<=ord(x)<=90:
        print(chr(25-(ord(x)-65)+65),end='')
    elif 97<=ord(x)<=122:
        print(chr(25-(ord(x)-97)+97),end='') 
    else:
        print(x,end='')      
