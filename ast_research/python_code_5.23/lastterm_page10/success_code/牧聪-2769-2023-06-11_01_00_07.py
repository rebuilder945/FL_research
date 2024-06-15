a = [chr(i) for i in (list(range(97, 123))+list(range(65,91)))]
b = [chr(i) for i in (list(range(122,96,-1))+list(range(90,64,-1)))]
zipped=zip(a,b)
LS=list(zipped)
LST=dict(LS)
words=input()
for x in words:
    if x not in LST:
        print(x,end='')
    else:
        print(LST[x],end='')
print(words)
