s=input()
sumA=ord("A")+ord("Z")
suma=ord("a")+ord("z")
ls1=list(s)
for i in range(len(s)):
    if s[i].isalpha() and s[i].isupper():
        n=sumA-ord(s[i])
        c=chr(n)
        ls1[i]=c
    if s[i].isalpha() and s[i].islower():
        n=suma-ord(s[i])
        c=chr(n)
        ls1[i]=c
print(s)
print("".join(ls1))

