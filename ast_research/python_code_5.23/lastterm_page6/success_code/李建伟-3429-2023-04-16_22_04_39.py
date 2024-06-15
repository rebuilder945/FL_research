s = input()
a = 0
b = 0
c = 0
d = 0
for i in s:
    if "a" <= i <= "z":
        a+=1
    elif i == " ":
        b+=1
    elif "1" <= i <= "9":
        c+=1
    else:
        d+=1
print(a,b,c,d)
