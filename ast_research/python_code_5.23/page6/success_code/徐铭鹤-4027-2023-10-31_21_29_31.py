sums=0
a=0
b=1
while(b):
    c=input()
    if(c!='#'):
        a+=1
        sums=sums+int(c)
    else:
        b=0
print(a,sums)

