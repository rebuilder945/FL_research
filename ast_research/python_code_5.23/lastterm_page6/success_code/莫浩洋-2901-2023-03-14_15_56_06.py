b=0
a=0

while 1:
    i= input()
    if i != "#":
        b+=int(i)
        a+=1
    else:
        break
print(a,b)
