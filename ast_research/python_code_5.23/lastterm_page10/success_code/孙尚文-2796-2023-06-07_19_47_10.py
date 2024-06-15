a=input()
b=""
c=""
for i in a:
    if i.isnumeric():
        b+=i
    else:
        if len(b)>=len(c):
            c=b
        b=''
if b=='':
    print("No digits")
else:
    print(c)
