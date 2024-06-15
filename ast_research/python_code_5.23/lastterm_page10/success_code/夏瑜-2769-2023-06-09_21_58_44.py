a=input()
print(a)
x=list(a)
d={}
for i in range(26):
    d[chr(ord("A")+i)]=chr(ord('A')+25-i)
    d[chr(ord("a")+i)]=chr(ord('a')+25-i)
for i in x:
    if i.isalpha()==True:
        c=d[i]
        print(c,end='')
    else:
        print(i,end='')


