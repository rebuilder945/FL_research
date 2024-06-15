a=0
b=0
c=0
aa="qwertyuioplkjhgfdsazxcvbnm"
bb="QWERTYUIOPLKJHGFDSAZXCVBNM"
cc="0123456789"
l=input()
for i in l :
    if i in aa:
        a=a+1
    elif i in bb:
        b=b+1
    elif i in cc:
        c=c+1
print(b)
print(a)
print(c)
