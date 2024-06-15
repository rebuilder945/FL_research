def zhao(s):
    ls=[]
    for x in range(len(s)-1):
        if s[x].isdigit()==False and s[x+1].isdigit()==True:
            ls.append(x+1)
        elif s[x].isdigit()==True and s[x+1].isdigit()==False:
            ls.append(x)
        elif s[x].isdigit()==True and s[x+1].isdigit()==True and x==0:
            ls.append(x)
        elif s[x].isdigit()==True and s[x+1].isdigit()==True and x+1==len(s)-1:
            ls.append(x+1)
    return ls
a=input()
b=zhao(a)
ls1=[]
ls2=[]
for x in range(0,len(b),2):
    c,d=b[x],b[x+1]
    ls1.append(a[c:d+1])
for x in ls1:
    d=len(x)
    ls2.append(d)
g=max(ls2)
ls1.reverse()
for x in ls1:
    if len(x)==g:
        print(x)
        break



