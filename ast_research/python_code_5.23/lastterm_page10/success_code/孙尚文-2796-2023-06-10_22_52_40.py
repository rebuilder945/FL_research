a=input()
b=""
c=""
for i in a:
    if i.isnumeric():
        b+=i
        if len(b)>=len(c):
            c=b
    if type(eval(i))!=int:
        b=""
if c=="":
    print("No digits")
else:
    print(c)
