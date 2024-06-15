s=input()
m=""
for i in s:
    if "a"<=i<="z":
        m+=chr(ord("a")+ord("z")-ord(i))
    elif "A"<=i<="Z":
        m+=chr(ord("A")+ord("Z")-ord(i))
    else:
        m+=i
print(s)
print(m)





