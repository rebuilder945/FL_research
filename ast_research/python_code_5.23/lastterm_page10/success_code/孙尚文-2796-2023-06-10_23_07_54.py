a=input()
b=""
c=""
for i in a:
    if i.isnumeric():
        b+=i
        if len(b)>=len(c):
            c=b
    if i>="9" or i <="0":
        b=""
if c=="":
    print("No digits")
else:
    print(c)
