#1
a = input()
b = ""
for i in a:
    if (int(i)+5)%10 !=0:
        b = b+str((int(i)+5)%10)
    else :
        b = b+"0"
b= b[::-1]
print(b)
