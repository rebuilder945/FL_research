a=input()
b=""
c=""
for x in a:
    if x.isnumeric():
        b+=x
    else:
        b=""
    if len(b)>=len(c):
        c=b
if c=="":
    print("No digits")
else:
    print(c)        
