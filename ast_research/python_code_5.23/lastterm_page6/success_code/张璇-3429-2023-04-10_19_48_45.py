a=list(input())
b=0
c=0
d=0
e=0
for x in range(len(a)):
    if a[x] in ['0','1','2','3','4','5','6','7','8','9']:
        b+=1
    elif a[x] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
        c+=1
    elif a[x] in [' ']:
        d+=1
    else:
        e+=1
print(c, b, d, e)
