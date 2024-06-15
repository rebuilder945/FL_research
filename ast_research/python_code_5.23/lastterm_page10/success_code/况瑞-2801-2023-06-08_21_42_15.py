a=input()
b=list(a)
c=r"~!@#$%^&*()_=-/,.?<>;:[]{}|\""
for i in range(len(b)):
    if b[i].isdigit():
        b[i]=1
    elif b[i].isalpha():
        if b[i].isupper():
            b[i]=2
        else:
            b[i]=3
    elif b[i] in c:
        b[i]=4
b=set(b)
if len(a)>=8:
    print(len(b)+1)
else:
    print(len(b))

    
    


