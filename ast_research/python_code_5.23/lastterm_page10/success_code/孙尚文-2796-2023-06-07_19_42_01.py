from re import I


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
if c=='':
    print("No digits")
else:
    print(c)
