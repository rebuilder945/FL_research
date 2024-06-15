n=list(input())
a,b,c,d=0,0,0,0
for i in n:
    if i.isalpha():
        a+=1
    elif i.isalnum():
        b+=1
    elif i.decimal():
        c+=1
    else:
        d+=1
print(a,b,c,d)
