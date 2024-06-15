len=0
s=0
while 1:
    x=input()
    if x=='#':
        break
    else:
        len+=1
        s+=int(x)
print(len,s)
