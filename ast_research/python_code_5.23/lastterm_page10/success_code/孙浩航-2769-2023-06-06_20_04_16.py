dic={}
for i in range(26):
    dic[chr(ord("A")+i)]=chr(ord("A")+25-i)
    dic[chr(ord("a")+i)]=chr(ord("a")+25-i)
a=input()
b=""
for x in a :
    if "a"<=x<="z" or "A"<=x<="Z":
        b+=dic[x]
    else:
        b+=x
print(a)
print(b)
