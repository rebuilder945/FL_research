def mi(a):
    q=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    p=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if a in q:
        for x in range(26):
            if q[x]==a:
                b=q[25-x]
        return b
    elif a in p:
        for x in range(26):
            if p[x]==a:
                b=p[25-x]
        return b         
    else:
        return a       
a=input()
print(a)
b=list(a)
for y in range(len(b)):
    b[y]=mi(b[y])
c="".join(b)
print(c)
