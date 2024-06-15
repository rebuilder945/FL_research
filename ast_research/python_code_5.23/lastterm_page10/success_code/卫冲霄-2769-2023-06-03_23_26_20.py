secret=input()
ls=[]
for i in secret:
    if  "A"<=i<="Z":
        i=chr(ord("A")-1+25+ord("A")-ord(i)+1)
        ls.append(i)
    elif "a"<=i<="z":
        i=chr(ord("a")-1+25+ord("a")-ord(i)+1)
        ls.append(i)
    else:
        ls.append(i)
print(secret)
text="".join(ls)
print(text)
