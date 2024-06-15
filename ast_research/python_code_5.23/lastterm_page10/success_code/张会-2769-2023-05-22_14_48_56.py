s=input()
print(s)
s1='abcdefghijklmnopkrstuvwxyz'
s2=s1[::-1]
s3=s1.upper()
s4=s3[::-1]
for i in s:
    if i.isalpha():
        if i==i.lower():
            m=s1.find(i)
            i=s2[m]
            print(i,end='')
        if i==i.upper():
            n=s3.find(i)
            i=s4[n]
            print(i,end='')
    else:
        print(i,end='')

