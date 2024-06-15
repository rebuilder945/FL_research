a=list(input())
for i in range(len(a)):
    if a[i]!='&':
        if a[i].islower():
            a[i]=chr(25-ord(a[i])+97*2)
        else:
            a[i]=chr(25-ord(a[i])+65*2)
for i in a:
    print(i,end='')
