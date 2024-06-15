a=input()
b=input()
c=""
for x in a:
    if x not in b:
        c=c+x
    else:
        c=c+""
print(c)
