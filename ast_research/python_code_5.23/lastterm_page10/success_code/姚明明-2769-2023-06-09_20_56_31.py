x=input()
print(x)
for i in x:
    if 'a'<=x<='z':
        print(chr(ord(i)+27),end="")
    elif 'A'<=x<='Z':
        print(chr(ord(i)+27),end="")
    else:
        print(i,end="")
    

