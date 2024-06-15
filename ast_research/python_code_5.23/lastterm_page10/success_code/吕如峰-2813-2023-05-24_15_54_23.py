s1=input()
s2=input()
flag=1
while flag==1:
    flag=0
    if s2 in s1:
        s1=s1.replace(s2,'')
        flag=1
print(s1)


