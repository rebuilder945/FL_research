uplist=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=list(input())
b=s[:]
print(''.join(str(i) for i in b))
for x in b:
    if x in uplist:
        m=uplist.index(str(x))
        print(uplist[25-m],end='')
    elif x in lowlist:
        n=lowlist.index(str(x))
        print(lowlist[25-n],end='')
    else:
        print(x,end='')
