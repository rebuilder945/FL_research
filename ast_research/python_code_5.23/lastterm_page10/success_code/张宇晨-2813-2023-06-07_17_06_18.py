a=input()
b=input()
c=""
for x in a:
    if x not in b:
        c=c+x
print(c)
