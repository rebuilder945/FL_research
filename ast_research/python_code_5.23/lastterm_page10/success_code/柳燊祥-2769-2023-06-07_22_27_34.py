uplist=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O,''P','Q','R','S','T','U','V','W','X','Y','Z']
lowlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input()
lst=list(s)
for x in lst:
    if x in uplist :
        m=uplist.index(x)
        x=uplist[25-m]
        print(x,end="")
    elif x in lowlist:
        n=lowlist.index(x)
        x=lowlist[25-n]
        print(x,end="")
    else:
        print(x,end="")
