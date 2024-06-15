s = input()
a = 0
b = 0
c = 0
d = 0
for n in s:
    if n.isalpha():
        a+=1
    elif n.isdigit():
        b+=1
    elif n.isspace():
        c+=1
    else:
        d+=1
print(a,c,b,d)





                    




