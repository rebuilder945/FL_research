secret=input()
str=""
for i in secret:
    if ord(i) in range(ord("A"),ord("Z")+1):
        i=chr(27+2*(ord("A")-1)-ord(i))
        str+=i
    elif ord(i) in range(ord("a"),ord("z")+1):
        i=chr(27+2*(ord("a")-1)-ord(i))
        str+=i
    else:
        str+=i
print(secret)
print(str)



