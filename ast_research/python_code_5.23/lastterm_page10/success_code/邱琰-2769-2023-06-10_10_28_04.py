n=list(input())
ls=[]
for i in n:
    if i.isalpha():
        if i.islower():
            i=chr(26-(ord(i)-ord('a')+1-1)+ord('a')-1)
            ls.append(i)
        else:
            i=chr(26-(ord(i)-ord('A')+1-1)+ord('A')-1)
            ls.append(i)
    else:
        ls.append(i)
print(''.join(n))
print(''.join(ls))
