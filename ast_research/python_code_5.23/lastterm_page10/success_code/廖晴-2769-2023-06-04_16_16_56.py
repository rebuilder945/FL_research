s=input()
print(s)
ss=list(s)
UP=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LOW=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in ss:
    if i in LOW:
        m=ss.index(str(i))
        print(LOW[25-m],end='')
    if i in UP:
        m=ss.index(str(i))
        print(UP[25-m],end='')
    else:
        pass
        print(i,end='')
