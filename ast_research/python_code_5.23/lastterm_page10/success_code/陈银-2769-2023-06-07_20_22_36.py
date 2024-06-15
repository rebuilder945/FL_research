def zhunhuan(x):
    if 97<=ord(x)<=122:
        y = chr(122-ord(x)+97)
        return y
    elif 65<=ord(x)<=90:
        y = chr(90-ord(x)+65)
        return y
    else:
        return x
a = input()
b=''
for x in a:
    b+=zhunhuan(x)
print(a)
print(b)
