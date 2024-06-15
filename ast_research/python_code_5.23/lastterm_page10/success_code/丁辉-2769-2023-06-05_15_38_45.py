a=input()
for x in a:
    if x.isalpha():
        x=chr(26+ord(x)-1)
        print(x,end='')
    else:
        print(x,end='')
            
