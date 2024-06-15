n = list(input())
a,b,c,d = 0,0,0,0
for i in n:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        b+=1
    elif i == ' ':
        c+=1
    else:
        d+=1
print(a,c,b,d)
