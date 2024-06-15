s1=input().split()
s2=input()
s3=s2.split()
for x in s3:
    for i in range(len(s1)):
        if x in s1[i]:
            s1[i]=s1[i].replace(s2,'')
            while ' ' in s1[i]:
                list(s1[i]).remove('')
                s1[i]=''.join(list(s1[i]))
        if ' ' not in s2:
            print(s1[i],end=' ')
        if ' ' in s2:
            print(s1[i],end='')


