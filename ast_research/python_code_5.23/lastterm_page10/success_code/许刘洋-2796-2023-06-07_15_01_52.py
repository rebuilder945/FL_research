a=input()
d=''
c=''
for i in a:
    if i.isdigit():
        d+=i
        if len(d)>=len(c):
            c=d
    else:
        d=''
print(c)

