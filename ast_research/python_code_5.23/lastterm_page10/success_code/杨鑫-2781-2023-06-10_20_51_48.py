a = input()
print(a)
for i in a:
    if ord(i)>= 97 and ord(i)<=122:
        b = chr(97+122-int(ord(i)))
        print(b,end="")
    elif ord(i)>=65 and ord(i)<=90:
        b = chr(65+90-int(ord(i)))
        print(b,end="")
    else:
        print(i,end="")
