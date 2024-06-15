a=0
c=0
b="1"
while   b!="#":
    b=input()
    if b!="#":
        a=a+eval(b)
        c+=1
print("{} {}".format(c,a))
