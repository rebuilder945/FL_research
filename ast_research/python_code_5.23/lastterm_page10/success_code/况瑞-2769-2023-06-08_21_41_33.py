b={}
for i in range(26):
    m=chr(ord("a")+i)
    n=chr(ord("a")+25-i)
    b[m]=n
for i in range(26):
    m=chr(ord("A")+i)
    n=chr(ord("A")+25-i)
    b[m]=n
n=input()
result=""
for i in n:
    if i.isalpha():
        result+=b[i]
    else:
        result+=i
print(n)
print(result)


