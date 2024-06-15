n = list(input())
a,b,c,d = 0,0,0,0
for i in n:
    if i in 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM':
        a+=1
    elif i in '1234567890':
        b+=1
    elif i == ' ':
        c+=1
    else:
        d+=1
print(a,c,b,d)
