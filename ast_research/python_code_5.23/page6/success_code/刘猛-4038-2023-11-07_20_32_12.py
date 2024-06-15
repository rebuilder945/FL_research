w = str(input())
e = 0
k = 0
n = 0
o = 0
for i in w:
    if i.isalpha():
        e+=1
    elif i.isspace():
        k+=1
    elif i.isdigit():
        n+=1
    else:
        o+=1
print(e,k,n,o)
