a=input()
b=""
c=""
for i in a:
    if i.isnumeric():
        b+=i
        if len(b)>=len(c):
            c=b
    if i.isalpha():
        b=""
if c=="":
    print("No digits")
else:
    print(c)
